"""

DOCSTRING

"""
import unittest
import os
import json
from pathlib import Path
from uc3m_care import VaccineManager
from uc3m_care import VaccineManagementException

class MyTestCase(unittest.TestCase):
    """
    Tests para los distintos casos de request_vaccination_id

    Los tests 1, 7, 8, 36, 39 y 40 son casos correctos. El resto son de error

    """
    def test1_request_vaccination_ok(self):
        """

        DOCSTRING

        """
        # Si ya existe el fichero json, se borra
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        my_request = VaccineManager()
        # Se comprueba que el código devuelto es correcto
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
            "Jose Johnson", "923412921", "45")
        self.assertEqual("cf58022264a00986e4654da43a7ab2d7", value)

        # Comprobamos el contenido del fichero json
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = [False, False, False, False, False]
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == \
                    "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found[0] = True
            if item["_VaccinePatientRegister__full_name"] == \
                    "Jose Johnson":
                found[1] = True
            if item["_VaccinePatientRegister__registration_type"] == \
                    "Regular":
                found[2] = True
            if item["_VaccinePatientRegister__phone_number"] == \
                    "923412921":
                found[3] = True
            if item["_VaccinePatientRegister__age"] == "45":
                found[4] = True
        for i in found:
            self.assertTrue(i)

    def test2_request_vaccination_notok_uuid1(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-113f-8eb9-dd262cfc54e0",
            "Regular", "Jose Johnson", "923412921", "45")
        self.assertEqual("Error: invalid UUID version", c_m.exception.message)

    def test3_request_vaccination_notok_uuid2(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("zbb5dbd6f-d8b4-113f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "923412921", "45")
        self.assertEqual("Error: invalid UUID", c_m.exception.message)

    def test4_request_vaccination_notok_uuid2(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("gghg", "Regular",
                "Jose Johnson", "923412921", "45")
        self.assertEqual("Error: invalid UUID", c_m.exception.message)

    def test5_request_vaccination_notok_uuid3(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id(None, "Regular",
                "Jose Johnson", "923412921", "45")
        self.assertEqual("Error: please enter a UUID", c_m.exception.message)

    def test6_request_vaccination_notok_uuid4(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id(99999, "Regular",
                "Jose Johnson", "923412921", "45")
        self.assertEqual("Error: UUID must be a string", c_m.exception.message)

    def test7_request_vaccination_ok(self):
        """

        DOCSTRING

        """
        # Si ya existe el fichero json, se borra
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        # Se comprueba que el código devuelto es correcto
        my_request = VaccineManager()
        value = my_request.request_vaccination_id("567f65de-5c03-4e8e-ae50-aa6b49b6893f",
        "Familiar", "Alfredo Sánchez", "666111222", "12")
        self.assertEqual("2212a8c2c0817ee54110f081ff7e14a2", value)

        # Comprobamos el contenido del fichero json
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = [False, False, False, False, False]
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == \
                    "567f65de-5c03-4e8e-ae50-aa6b49b6893f":
                found[0] = True
            if item["_VaccinePatientRegister__full_name"] == "Alfredo Sánchez":
                found[1] = True
            if item["_VaccinePatientRegister__registration_type"] == "Familiar":
                found[2] = True
            if item["_VaccinePatientRegister__phone_number"] == "666111222":
                found[3] = True
            if item["_VaccinePatientRegister__age"] == "12":
                found[4] = True
        for i in found:
            self.assertTrue(i)

    def test8_request_vaccination_ok(self):
        """

        DOCSTRING

        """
        #Abrimos el fichero para comprobar las entradas después
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        #Se comprueba que el código devuelto es correcto
        my_request = VaccineManager()
        value = my_request.request_vaccination_id("eb6cb027-08e9-4d11-bc85-dabf844bae22",
            "Familiar", "Pedro Soni", "552555222", "56")
        self.assertEqual("a6c600c150eb5b240168ddab1d73b235", value)

        #Comprobamos el contenido del fichero json
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = [False, False, False, False, False]
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == \
                    "eb6cb027-08e9-4d11-bc85-dabf844bae22":
                found[0] = True
            if item["_VaccinePatientRegister__full_name"] == \
                    "Pedro Soni":
                found[1] = True
            if item["_VaccinePatientRegister__registration_type"] == \
                    "Familiar":
                found[2] = True
            if item["_VaccinePatientRegister__phone_number"] == \
                    "552555222":
                found[3] = True
            if item["_VaccinePatientRegister__age"] == \
                    "56":
                found[4] = True
        for i in found:
            self.assertTrue(i)

    def test9_request_vaccination_notok_reg1(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Perros", "Toby Woof", "923412921", "8")
        self.assertEqual("Error: invalid registration type", c_m.exception.message)

    def test10_request_vaccination_notok_reg1(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "p231m2", "Toby Woof", "923412921", "8")
        self.assertEqual("Error: invalid registration type", c_m.exception.message)

    def test11_request_vaccination_notok_reg2(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                234231, "Toby Woof", "923412921", "8")
        self.assertEqual("Error: registration type must be a string", c_m.exception.message)

    def test12_request_vaccination_notok_reg2(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                231.123, "Toby Woof", "923412921", "8")
        self.assertEqual("Error: registration type must be a string", c_m.exception.message)

    def test13_request_vaccination_notok_reg3(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                None, "Toby Woof", "923412921", "8")
        self.assertEqual("Error: registration type can't be null", c_m.exception.message)

    def test14_request_vaccination_notok_name1(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Federicogonzaloramonperecianorodríguez", "923412921", "45")
        self.assertEqual("Error: name is too long", c_m.exception.message)

    def test15_request_vaccination_notok_name2(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Juan Nepomuceno96", "923412921", "45")
        self.assertEqual("Error: name must have two words, "
                "separated by a space and contain no digits", c_m.exception.message)

    def test16_request_vaccination_notok_name2(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "198Juan Nepomuceno", "923412921", "45")
        self.assertEqual("Error: name must have two words, "
                "separated by a space and contain no digits", c_m.exception.message)

    def test17_request_vaccination_notok_name3(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Feliciano", "923412921", "45")
        self.assertEqual("Error: name must have two words, "
                "separated by a space and contain no digits", c_m.exception.message)

    def test18_request_vaccination_notok_name4(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Pepe González de la Santa Sal", "923412921", "45")
        self.assertEqual("Error: name must have two words, "
                "separated by a space and contain no digits", c_m.exception.message)

    def test19_request_vaccination_notok_name4(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Nombre muy Incorrecto", "923412921", "45")
        self.assertEqual("Error: name must have two words, "
                "separated by a space and contain no digits", c_m.exception.message)

    def test20_request_vaccination_notok_name5(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", 2341231, "923412921", "45")
        self.assertEqual("Error: name must be a string", c_m.exception.message)

    def test21_request_vaccination_notok_number1(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "99123", "45")
        self.assertEqual("Error: number must contain 9 characters and only numerals",
            c_m.exception.message)

    def test22_request_vaccination_notok_number1(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "0", "45")
        self.assertEqual("Error: number must contain 9 characters and only numerals",
                c_m.exception.message)

    def test23_request_vaccination_notok_number1(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "", "45")
        self.assertEqual("Error: no phone number", c_m.exception.message)

    def test24_request_vaccination_notok_number2(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "23424534324", "45")
        self.assertEqual("Error: number must contain 9 characters and only numerals",
                c_m.exception.message)

    def test25_request_vaccination_notok_number3(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "Esteesmino", "45")
        self.assertEqual("Error: number must contain 9 characters and only numerals",
                c_m.exception.message)

    def test26_request_vaccination_notok_number3(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "234num2323", "45")
        self.assertEqual("Error: number must contain 9 characters and only numerals",
                c_m.exception.message)

    def test27_request_vaccination_notok_number4(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", None, "45")
        self.assertEqual("Error: no phone number", c_m.exception.message)

    def test28_request_vaccination_notok_number5(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", 24.67, "45")
        self.assertEqual("Error: number must be a string", c_m.exception.message)

    def test29_request_vaccination_notok_age1(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "685838390", "5")
        self.assertEqual("Error: age must be between 6 and 125", c_m.exception.message)

    def test30_request_vaccination_notok_age1(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "685838390", "-3241")
        self.assertEqual("Error: age string must only contain a number from 6 to 125",
                c_m.exception.message)

    def test31_request_vaccination_notok_age2(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "685838390", "126")
        self.assertEqual("Error: age must be between 6 and 125", c_m.exception.message)

    def test32_request_vaccination_notok_age2(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "685838390", "9999")
        self.assertEqual("Error: age must be between 6 and 125", c_m.exception.message)

    def test33_request_vaccination_notok_age2(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "685838390", "64.35")
        self.assertEqual("Error: age string must only contain a number from 6 to 125",
                c_m.exception.message)

    def test34_request_vaccination_notok_age2(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "685838390", "32.00")
        self.assertEqual("Error: age string must only contain a number from 6 to 125",
                c_m.exception.message)

    def test35_request_vaccination_notok_age3(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "685838390", "stringnum")
        self.assertEqual("Error: age string must only contain a number from 6 to 125",
            c_m.exception.message)

    def test36_request_vaccination_ok(self):
        """

        DOCSTRING

        """
        # Si ya existe el fichero json, se borra
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        #Comprobamos el valor del código devuelto
        my_request = VaccineManager()
        value = my_request.request_vaccination_id("cb3dd087-0868-4203-bbbd-5e7899fbbe2a", "Regular",
            "Rosa García", "678923456", "34")
        self.assertEqual("04ef57001189019ce49f9344cc92a78a", value)

        # Comprobamos el contenido del fichero json
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = [False, False, False, False, False]
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == \
                    "cb3dd087-0868-4203-bbbd-5e7899fbbe2a":
                found[0] = True
            if item["_VaccinePatientRegister__full_name"] == \
                    "Rosa García":
                found[1] = True
            if item["_VaccinePatientRegister__registration_type"] == \
                    "Regular":
                found[2] = True
            if item["_VaccinePatientRegister__phone_number"] == \
                    "678923456":
                found[3] = True
            if item["_VaccinePatientRegister__age"] == \
                    "34":
                found[4] = True
        for i in found:
            self.assertTrue(i)

    def test37_request_vaccination_notok_uuid4(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id(None, "Regular",
                                                      "Jose Johnson", "923412921", "45")
        self.assertEqual("Error: please enter a UUID", c_m.exception.message)

    def test38_request_vaccination_notok_name6(self):
        """

        DOCSTRING

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", None, "923412921", "45")
        self.assertEqual("Error: name can't be null", c_m.exception.message)

    def test39_request_vaccination_ok(self):
        """

        DOCSTRING

        """
        # Si ya existe el fichero json, se borra
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        # Comprobamos el valor del código devuelto
        my_request = VaccineManager()
        value = my_request.request_vaccination_id("31e68fe8-13dd-4dd3-9b81-69a66cb80a91",
            "Familiar", "Esternilocideo Masterianosones", "000000000", "6")
        self.assertEqual("9a1138a3e918ced64d7d05795798ee0a", value)

        # Comprobamos el contenido del fichero json
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = [False, False, False, False, False]
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == \
                    "31e68fe8-13dd-4dd3-9b81-69a66cb80a91":
                found[0] = True
            if item["_VaccinePatientRegister__full_name"] == \
                    "Esternilocideo Masterianosones":
                found[1] = True
            if item["_VaccinePatientRegister__registration_type"] == \
                    "Familiar":
                found[2] = True
            if item["_VaccinePatientRegister__phone_number"] == \
                    "000000000":
                found[3] = True
            if item["_VaccinePatientRegister__age"] == \
                    "6":
                found[4] = True
        for i in found:
            self.assertTrue(i)

    def test40_request_vaccination_ok(self):
        """

        DOCSTRING

        """
        # Si ya existe el fichero json, se borra
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        # Comprobamos el valor del código devuelto
        my_request = VaccineManager()
        value = my_request.request_vaccination_id("9f159456-9a1c-4bd4-a1e3-b2f181c86b6c", "Regular",
            "C J", "918234765", "125")
        self.assertEqual("4bfe2cc688ee752991718af264c18c6d", value)

        # Comprobamos el contenido del fichero json
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = [False, False, False, False, False]
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == \
                    "9f159456-9a1c-4bd4-a1e3-b2f181c86b6c":
                found[0] = True
            if item["_VaccinePatientRegister__full_name"] == \
                    "C J":
                found[1] = True
            if item["_VaccinePatientRegister__registration_type"] == \
                    "Regular":
                found[2] = True
            if item["_VaccinePatientRegister__phone_number"] == \
                    "918234765":
                found[3] = True
            if item["_VaccinePatientRegister__age"] == \
                    "125":
                found[4] = True
        for i in found:
            self.assertTrue(i)


if __name__ == '__main__':
    unittest.main()
