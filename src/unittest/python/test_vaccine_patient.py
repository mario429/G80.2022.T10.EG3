"""

DOCSTRING

"""

import unittest
import os
import json
from datetime import datetime
from pathlib import Path
from uc3m_care import VaccineManager
from uc3m_care import VaccineManagementException
from freezegun import freeze_time

@freeze_time("2022-06-06")
class MyTestCase(unittest.TestCase):
    """

    This class groups the tests related to the vaccine patient method

    """
    def test1_vaccine_patient_ok(self):
        """

        DOCSTRING

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
        this_id = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                    "Regular", "Jose Johnson", "923412921", "45")
        value = my_request.get_vaccine_date(file_test)

        try:
            with open(file_store_date, 'r', encoding="utf-8", newline="") as file:
                data_list = json.load(file)

        except FileNotFoundError:
            data_list = []

        this_vaccine = my_request.vaccine_patient(data_list[0]["_VaccinationAppoinment__date_signature"])
        self.assertEqual(True, this_vaccine)


    def test2_vaccine_patient_vaccinated(self):
        """

        DOCSTRING

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

        this_id = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                    "Regular", "Jose Johnson", "923412921", "45")
        value = my_request.get_vaccine_date(file_test)

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

        DOCSTRING

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
        this_id = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                    "Regular", "Jose Johnson", "923412921", "45")
        value = my_request.get_vaccine_date(file_test)

        try:
            with open(file_store_date, 'r', encoding="utf-8", newline="") as file:
                data_list = json.load(file)

        except FileNotFoundError:
            data_list = []

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.vaccine_patient(r"f96386153f2767f620e5bacdf1d33W278fabe54bf4d43e7acb172233131de254")
        self.assertEqual("Error: invalid Patient's date_signature' --> "
            "Signature does not match with regex", c_m.exception.message)


    def test4_vaccine_patient_signature_not_found(self):
        """

        DOCSTRING

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
        this_id = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                    "Regular", "Jose Johnson", "923412921", "45")
        value = my_request.get_vaccine_date(file_test)

        try:
            with open(file_store_date, 'r', encoding="utf-8", newline="") as file:
                data_list = json.load(file)

        except FileNotFoundError:
            data_list = []

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.vaccine_patient(r"f96386153f2767f620e5bacdf1d33f278fabe54bf4d43e7acb172233131de254")
        self.assertEqual("Error: date_signature doesn't exist in the system", c_m.exception.message)

    def test5_vaccine_patient_date_not_today(self):
        """

        DOCSTRING

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

        this_id = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                    "Regular", "Jose Johnson", "923412921", "45")
        value = my_request.get_vaccine_date(file_test)

        try:
            with open(file_store_date, 'r', encoding="utf-8", newline="") as file:
                data_list = json.load(file)

        except FileNotFoundError:
            data_list = []

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.vaccine_patient(data_list[0]["_VaccinationAppoinment__date_signature"], 1255337600.0)
        self.assertEqual("Error: actual date doesn't match with "
            "the issued vaccination date", c_m.exception.message)


    def test6_vaccine_patient_signature_string(self):
        """

        DOCSTRING

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

        this_id = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                    "Regular", "Jose Johnson", "923412921", "45")
        value = my_request.get_vaccine_date(file_test)

        try:
            with open(file_store_date, 'r', encoding="utf-8", newline="") as file:
                data_list = json.load(file)

        except FileNotFoundError:
            data_list = []

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.vaccine_patient(123456789239239868573)
        self.assertEqual("Error: invalid Patient's date_signature' "
            "--> Signature's data type is not String", c_m.exception.message)

    def test7_vaccine_patient_signature_not64(self):
        """

        DOCSTRING

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

        this_id = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                    "Regular", "Jose Johnson", "923412921", "45")
        value = my_request.get_vaccine_date(file_test)

        try:
            with open(file_store_date, 'r', encoding="utf-8", newline="") as file:
                data_list = json.load(file)

        except FileNotFoundError:
            data_list = []

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.vaccine_patient(r"d43e7acb172233131de254")
        self.assertEqual("Error: invalid Patient's date_signature "
            "--> Signature must have 64 bytes", c_m.exception.message)

if __name__ == '__main__':
    unittest.main()
