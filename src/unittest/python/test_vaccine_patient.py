"""

Fichero que contiene los tests asociados a la función vaccine_patient()

"""

import unittest
import os
import json
from pathlib import Path
from uc3m_care import VaccineManager
from uc3m_care import VaccineManagementException
from freezegun import freeze_time

@freeze_time("2022-06-06")
class MyTestCase(unittest.TestCase):
    """

    Esta clase agrupa los distintos tests estructurales

    """
    def test1_vaccine_patient_ok(self):
        """

        Test 1 que realiza el procedimiento de inserción de una vacunación

        """
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"
        file_store_date = json_path + "store_patient_date.json"
        file_store_vaccine_patient = json_path + "store_vaccine_patient.json"
        file_test = json_path + "tests_get_vaccine_date/test1_get_vaccine_date_ok.json"

        if os.path.isfile(file_store):
            os.remove(file_store)
        if os.path.isfile(file_store_date):
            os.remove(file_store_date)
        if os.path.isfile(file_store_vaccine_patient):
            os.remove(file_store_vaccine_patient)

        my_request = VaccineManager()
        my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                    "Regular", "Jose Johnson", "923412921", "45")
        my_request.get_vaccine_date(file_test)

        try:
            with open(file_store_date, 'r', encoding="utf-8", newline="") as file:
                data_list = json.load(file)

        except FileNotFoundError:
            data_list = []

        this_vaccine = my_request.vaccine_patient(
            data_list[0]["_VaccinationAppoinment__date_signature"])
        self.assertEqual(True, this_vaccine)


    def test2_vaccine_patient_vaccinated(self):
        """

        Test 2 que falla al recibir un paciente ya vacunado

        """
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test1_get_vaccine_date_ok.json"

        if os.path.isfile(file_store):
            os.remove(file_store)
        if os.path.isfile(file_store_date):
            os.remove(file_store_date)

        my_request = VaccineManager()

        my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                    "Regular", "Jose Johnson", "923412921", "45")
        my_request.get_vaccine_date(file_test)

        try:
            with open(file_store_date, 'r', encoding="utf-8", newline="") as file:
                data_list = json.load(file)

        except FileNotFoundError:
            data_list = []

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.vaccine_patient(data_list[0]["_VaccinationAppoinment__date_signature"])
        self.assertEqual("Error: Patient has already been vaccinated", c_m.exception.message)

    def test3_vaccine_patient_invalid_signature(self):
        """

        Test 3 que falla al recibir un hash inválido

        """
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"
        file_store_date = json_path + "store_patient_date.json"
        file_store_vaccine_patient = json_path + "store_vaccine_patient.json"
        file_test = json_path + "tests_get_vaccine_date/test1_get_vaccine_date_ok.json"

        if os.path.isfile(file_store):
            os.remove(file_store)
        if os.path.isfile(file_store_date):
            os.remove(file_store_date)
        if os.path.isfile(file_store_vaccine_patient):
            os.remove(file_store_vaccine_patient)

        my_request = VaccineManager()
        my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                    "Regular", "Jose Johnson", "923412921", "45")
        my_request.get_vaccine_date(file_test)

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.vaccine_patient(
                r"f96386153f2767f620e5bacdf1d33W278fabe54bf4d43e7acb172233131de254")
        self.assertEqual("Error: invalid Patient's date_signature' --> "
            "Signature does not match with regex", c_m.exception.message)


    def test4_vaccine_patient_signature_not_found(self):
        """

        Test 4 que falla al no encontrar el hash en el almacén

        """
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"
        file_store_date = json_path + "store_patient_date.json"
        file_store_vaccine_patient = json_path + "store_vaccine_patient.json"
        file_test = json_path + "tests_get_vaccine_date/test1_get_vaccine_date_ok.json"

        if os.path.isfile(file_store):
            os.remove(file_store)
        if os.path.isfile(file_store_date):
            os.remove(file_store_date)
        if os.path.isfile(file_store_vaccine_patient):
            os.remove(file_store_vaccine_patient)

        my_request = VaccineManager()
        my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                    "Regular", "Jose Johnson", "923412921", "45")
        my_request.get_vaccine_date(file_test)

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.vaccine_patient(
                r"f96386153f2767f620e5bacdf1d33f278fabe54bf4d43e7acb172233131de254")
        self.assertEqual("Error: date_signature doesn't exist in the system", c_m.exception.message)

    def test5_vaccine_patient_date_not_today(self):
        """

        Test que falla al no coincidir la fecha de vacunación con la actual (freeze)

        """
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"
        file_store_date = json_path + "store_patient_date.json"
        file_store_vaccine_patient = json_path + "store_vaccine_patient.json"
        file_test = json_path + "tests_get_vaccine_date/test1_get_vaccine_date_ok.json"

        if os.path.isfile(file_store):
            os.remove(file_store)
        if os.path.isfile(file_store_date):
            os.remove(file_store_date)
        if os.path.isfile(file_store_vaccine_patient):
            os.remove(file_store_vaccine_patient)

        my_request = VaccineManager()

        my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                    "Regular", "Jose Johnson", "923412921", "45")
        my_request.get_vaccine_date(file_test)

        try:
            with open(file_store_date, 'r', encoding="utf-8", newline="") as file:
                data_list = json.load(file)

        except FileNotFoundError:
            data_list = []

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.vaccine_patient(
                data_list[0]["_VaccinationAppoinment__date_signature"], 1255337600.0)
        self.assertEqual("Error: actual date doesn't match with "
            "the issued vaccination date", c_m.exception.message)


   # EL SIGUIENTE PAR DE TESTS ESTÁ PENSADO PARA COMPROBAR
   # LAS 2 EXCEPCIONES QUE DEVOLVERÍA LA SUBRUTINA validate_date_signature()


    def test6_vaccine_patient_signature_string(self):
        """

        Test que falla al recibir hash que no se encuentra en el tipo String

        """
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"
        file_store_date = json_path + "store_patient_date.json"
        file_store_vaccine_patient = json_path + "store_vaccine_patient.json"
        file_test = json_path + "tests_get_vaccine_date/test1_get_vaccine_date_ok.json"

        if os.path.isfile(file_store):
            os.remove(file_store)
        if os.path.isfile(file_store_date):
            os.remove(file_store_date)
        if os.path.isfile(file_store_vaccine_patient):
            os.remove(file_store_vaccine_patient)

        my_request = VaccineManager()

        my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                    "Regular", "Jose Johnson", "923412921", "45")
        my_request.get_vaccine_date(file_test)

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.vaccine_patient(123456789239239868573)
        self.assertEqual("Error: invalid Patient's date_signature' "
            "--> Signature's data type is not String", c_m.exception.message)

    def test7_vaccine_patient_signature_not64(self):
        """

        Test que falla al recibir un hash que no cumple con la longitud de 64 bytes

        """
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"
        file_store_date = json_path + "store_patient_date.json"
        file_store_vaccine_patient = json_path + "store_vaccine_patient.json"
        file_test = json_path + "tests_get_vaccine_date/test1_get_vaccine_date_ok.json"

        if os.path.isfile(file_store):
            os.remove(file_store)
        if os.path.isfile(file_store_date):
            os.remove(file_store_date)
        if os.path.isfile(file_store_vaccine_patient):
            os.remove(file_store_vaccine_patient)

        my_request = VaccineManager()

        my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                    "Regular", "Jose Johnson", "923412921", "45")
        my_request.get_vaccine_date(file_test)

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.vaccine_patient(r"d43e7acb172233131de254")
        self.assertEqual("Error: invalid Patient's date_signature "
            "--> Signature must have 64 bytes", c_m.exception.message)

if __name__ == '__main__':
    unittest.main()
