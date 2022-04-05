"""

File contains the set of tests related to the function "get_vaccine_date()"

"""
import unittest
import os
import json
import hashlib
from pathlib import Path
from uc3m_care import VaccineManager
from uc3m_care import VaccineManagementException
from freezegun import freeze_time

@freeze_time("2022-06-06") # Congelamos el tiempo para que la hora sea siempre la misma en los tests

class MyTestCase2(unittest.TestCase):
    """

    Tests para los distintos casos de get_vaccine_date()

    """
    def test1_get_vaccine_date_ok(self):
        """

        Test 1 con el proceso de obtener un hash de 64 bytes correcto

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

    def test_all(self):
        """

        Este método testea todos los ficheros json de formato incorrecto.

        """
        #Directorio con todos los ficheros json
        files = os.listdir(str(Path.home()) +
            "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/tests_get_vaccine_date/")
        for i in files:
            if i != "test1_get_vaccine_date_ok.json":
                print("Testing " + i)
                self.test_incorrect(i)
                print("OK!")

    def test_incorrect(self, test_path=None):
        """

        Test auxiliar a test_all.

        """
        if test_path: #Si no se ha llamado con un valor de test_path, se ignora el test

            json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
            file_store_date = json_path + "store_patient_date.json"
            file_test = json_path + "tests_get_vaccine_date/" + test_path
            #Abrimos el fichero original para comprobar luego que no cambia

            with open(file_store_date, "r", encoding="utf-8", newline="") as file_org:
                hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()

            #Comprobamos error
            with self.assertRaises(VaccineManagementException) as c_m:
                my_request = VaccineManager()
                my_request.get_vaccine_date(file_test)
            self.assertEqual("Wrong json file format", c_m.exception.message)
            #Vemos que no cambia el fichero
            with open(file_store_date, "r", encoding="utf-8", newline="") as file_org:
                hash_new = hashlib.md5(file_org.__str__().encode()).hexdigest()
            self.assertEqual(hash_original, hash_new)

if __name__ == '__main__':
    unittest.main()
