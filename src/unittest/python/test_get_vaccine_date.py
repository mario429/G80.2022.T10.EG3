"""

DOCSTRING

"""
import unittest
import os
import json
import hashlib
from pathlib import Path
from uc3m_care import VaccineManager
from uc3m_care import VaccineManagementException
from freezegun import freeze_time

@freeze_time("2022-06-06") #Congelamos el tiempo para que la hora sea siempre la misma en los tests

class MyTestCase2(unittest.TestCase):
    """
    Tests para los distintos casos de get_vaccine_date

    """
    def test1_get_vaccine_date_ok(self):
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
        this_id = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                          "Jose Johnson", "923412921", "45")

        value = my_request.get_vaccine_date(file_test)
        self.assertEqual(value, "f96386153f2767f620e5bacdf1d33b278fabe54bf4d43e7acb172233131de254")

        #Comprobamos que se ha añadido
        with open(file_store_date, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_VaccinationAppoinment__patient_sys_id"] == \
                    this_id:
                found = True
        self.assertTrue(found)

    def test_vacio(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_vacio.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_doble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_primer_bracket(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sinprimercorchete.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_primer_bracket_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_primerbracketdoble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_solo_corchetes(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_solocorchetes.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_datos_dobles(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_datosdobles.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_segundo_bracket_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_segundobracketdoble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_segundo_bracket(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sinsegundobracket.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_primer_campo_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_primercampodoble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_primer_campo(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sinprimercampo.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_primer_campo(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sinprimercampo.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_coma(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sincoma.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_coma_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_comadoble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_segundo_campo_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_segundocampodoble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_segundo_campo(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sinsegundocampo.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_primera_etiqueta_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_primeraetiquetadoble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_primera_etiqueta(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sinprimeraetiqueta.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_igualdad1(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sinigualdad1.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_igualdad1_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_igualdad1doble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_dato1_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_dato1doble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_dato1(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sindato1.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_segunda_etiqueta_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_segundaetiquetadoble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_segunda_etiqueta(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sinsegundaetiqueta.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_igualdad2_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_igualdad2doble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_igualdad2(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sinigualdad2.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_dato2_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_dato2doble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_dato2(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sindato2.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_comilla1(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sincomilla1.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_comilla1_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_coilla1doble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_valor_etiqueta1_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_valoretiqueta1doble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_comilla2_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_comilla2doble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_comilla2(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sincomilla2.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_comilla3_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_comilla3doble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_comilla3(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sincomilla3.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_comilla4doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_comilla4doble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_comilla4(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sincomilla4.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_valor_dato1_duplicado(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_valordato1duplicado.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_valor_etiqueta2_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_valoretiqueta2doble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_valor_dato2_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_valordato2doble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_comilla5(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sincomilla5.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_comilla5_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_comilla5doble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_comilla6(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sincomilla6.json"
        # Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding="utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        # Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        # Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding="utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_comilla7(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sincomilla7.json"
        # Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding="utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        # Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        # Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding="utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_comilla7_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_comilla7doble.json"
        # Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding="utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        # Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        # Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding="utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_sin_comilla8(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_sincomilla8.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)

    def test_comilla8_doble(self):
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"
        file_test = json_path + "tests_get_vaccine_date/test_comilla8doble.json"
        #Abrimos el fichero original para comprobar luego que no cambia
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
        #Comprobamos error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request = VaccineManager()
            my_request.get_vaccine_date(file_test)
        self.assertEqual("Wrong json file format", c_m.exception.message)
        #Vemos que no cambia el fichero
        with open(file_store_date, "r", encoding = "utf-8", newline="") as file_org:
            hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash_new)



if __name__ == '__main__':
    unittest.main()