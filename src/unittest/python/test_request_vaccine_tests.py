# pylint: disable=R0904
"""

Este fichero contiene todos los tests unitarios asociados a request_vaccine_tests()

"""
import unittest
import os
import json
from pathlib import Path
from uc3m_care import VaccineManager
from uc3m_care import VaccineManagementException
from freezegun import freeze_time

@freeze_time("2022-06-06") # Congelamos el tiempo para que la hora sea siempre la misma en los tests

class MyTestCase(unittest.TestCase):
    """

    Clase que recoge los tests que resultan en fallos o éxitos según su finalidad


    """
    def test1_request_vaccination_ok(self):
        """

        Test que comprueba si los datos necesarios para solicitar la
        vacunación son correctos. El test devuelve
        un resultado correcto.

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
        self.assertEqual("5c6824ff32c328161e44d963d4f95c7f", value)

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

        Test que comprueba que se devuelve un error cuando se utiliza una
        UUID correcta pero desactualizada (antigua).

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-113f-8eb9-dd262cfc54e0",
            "Regular", "Jose Johnson", "923412921", "45")
        self.assertEqual("Error: invalid UUID version", c_m.exception.message)

    def test3_request_vaccination_notok_uuid2(self):
        """

        Test que comprueba que se devuelve un error cuando el UUID
        NO es correcto (caracter extra añadido para provocar el fallo).

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("zbb5dbd6f-d8b4-113f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "923412921", "45")
        self.assertEqual("Error: invalid UUID", c_m.exception.message)


    def test4_request_vaccination_notok_uuid4(self):
        """

        Test que comprueba que se devuelve un error cuando el
        UUID NO es un String (se usa un número entero para provocar
        el fallo).

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id(99999, "Regular",
                "Jose Johnson", "923412921", "45")
        self.assertEqual("Error: invalid UUID", c_m.exception.message)

    def test5_request_vaccination_ok(self):
        """

        Test que resulta correcto al comprobar todos los datos
        (correctos) de un usuario.

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
        self.assertEqual("598cb2e44f90d0452f901f63a6a97579", value)

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

    def test6_request_vaccination_ok(self):
        """

        Test que resulta correcto al comprobar todos los datos (correctos)
        de otro usuario. Test similar al anterior pero con otro conjunto
        de datos.

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
        self.assertEqual("5db2aae9bbec96f00e2dfeabd10b6ba7", value)

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

    def test7_request_vaccination_notok_reg1(self):
        """

        Test que comprueba que se devuelve un error cuando el
        "registration type" no es ni "Familiar" ni "Regular.

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Perros", "Toby Woof", "923412921", "8")
        self.assertEqual("Error: registration_type "
                         "must be 'Familiar' or 'Regular'", c_m.exception.message)

    def test8_request_vaccination_notok_reg2(self):
        """

        Test que comprueba que se devuelve un error cuando el
        "registration type" no es ni "Familiar" ni "Regular. Para
        este test se utiliza un número como "registration type"

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                234231, "Toby Woof", "923412921", "8")
        self.assertEqual("Error: registration_type must be "
                         "'Familiar' or 'Regular'", c_m.exception.message)

    def test9_request_vaccination_notok_name1(self):
        """

        Test que devuelve un error cuando se introduce un nombre cuya longitud
        es superior a los 30 caracteres.

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "UnNombreDeMas TreintaCaracteres", "923412921", "45")
        self.assertEqual("Error: name is too long", c_m.exception.message)

    def test10_request_vaccination_notok_name3(self):
        """

        Test que devuelve un error cuando el formato del nombre NO es correcto.
        El formato correcto es <name>+<surname>

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Feliciano", "923412921", "45")
        self.assertEqual("Error: wrong name format", c_m.exception.message)

    def test11_request_vaccination_notok_name4(self):
        """

        Test que devuelve un error cuando el formato del nombre NO es correcto.
        En este caso el nombre tiene demasiados términos.

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Pepe González de la Santa Sal", "923412921", "45")
        self.assertEqual("Error: wrong name format", c_m.exception.message)

    def test12_request_vaccination_notok_number1(self):
        """

        Test que devuelve un error cuando el teléfono introducido es demasiado corto.

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "12345678", "45")
        self.assertEqual("Error: number must "
                         "contain 9 characters and only digits", c_m.exception.message)

    def test13_request_vaccination_notok_number2(self):
        """

        Test que devuelve un error cuando el teléfono introducido es demasiado largo.

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "9123456789", "45")
        self.assertEqual("Error: number must contain "
                         "9 characters and only digits",c_m.exception.message)

    def test14_request_vaccination_notok_number3(self):
        """

        Test que devuelve un error cuando el teléfono no sigue el formato adecuado.
        Se introduce un String que incluye letras para provocar dicho fallo.

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "Esteesmino", "45")
        self.assertEqual("Error: number must contain 9 characters and only digits",
                c_m.exception.message)

    def test15_request_vaccination_notok_age1(self):
        """

        Test que devuelve un error cuando la edad introducida es menor que la mínima
        requerida (6 años). Para el test se introducirá 5 años.

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "685838390", "5")
        self.assertEqual("Error: age must be between 6 and 125", c_m.exception.message)


    def test16_request_vaccination_notok_age2(self):
        """

        Test que devuelve un error cuando la edad introducida es mayor a la máxima permitida.
        Para el test se utilizará 126 años (siendo el límite 125 años).

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "685838390", "126")
        self.assertEqual("Error: age must be between 6 and 125", c_m.exception.message)


    def test17_request_vaccination_notok_age2(self):
        """

        Test que devuelve un error cuando la edad introducida no sigue el formato adecuado,
        introduciendo decimales en el valor (el formato NO debe contener decimales, será
        un String únicamente con números).

        """
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                "Regular", "Jose Johnson", "685838390", "64.35")
        self.assertEqual("Error: invalid age format",
                c_m.exception.message)

    def test18_request_vaccination_ok(self):
        """

        Test que comprueba la correcta validación de los datos de un usuario nuevo.
        Este test es similar al número 1.

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
        self.assertEqual("7c40f9678455c60012361935258f8f8f", value)

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

    def test19_request_vaccination_ok(self):
        """

        Test que resulta exitoso al introducir un usuario con los valores límite
        de nombre (30 caracteres) y edad (mínimo 6 años)

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
        self.assertEqual("07b2ec8ee2978df11669d141dfd89deb", value)

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

    def test20_request_vaccination_ok(self):
        """

        Test que resulta exitoso al introducir un usuario con los valores límite
        de nombre (en este caso, el nombre mínimo: 1 caracter por nombre y 1 caracter
        por apellido) y la edad máxima (125 años).

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
        self.assertEqual("bba81a26c24676a407442b0f091f7bd4", value)

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

    def test21_request_vaccination_ok(self):
        """

        Test que resulta exitoso al introducir un mismo paciente con el
        "registration type" regular y familiar, no se produce error.

        """
        # Si ya existe el fichero json, se borra
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        # Creamos un código correcto para que se guarde en el fichero json
        my_request1 = VaccineManager()
        my_request1.request_vaccination_id("6707dad0-c806-4901-87cf-d2e161618f56",
            "Regular", "Marco Pedro", "925902123", "89")
        # Ahora creamos el mismo para comprobar si da error
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request1 = VaccineManager()
            my_request1.request_vaccination_id("6707dad0-c806-4901-87cf-d2e161618f56",
                "Regular", "Marco Pedro", "925902123", "89")
        self.assertEqual("Error: patient ID already registered", c_m.exception.message)

    def test22_request_vaccination_ok(self):
        """

        Test que devuelve un error al intentar introducir un mismo paciente.
        Al haber registrado ya al paciente con ambos "registration type",
        el resultado al intentar introducirlo de nuevo es un error.

        """
        # Si ya existe el fichero json, se borra
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        # Creamos un código correcto para que se guarde en el fichero
        my_request1 = VaccineManager()
        my_request1.request_vaccination_id("6707dad0-c806-4901-87cf-d2e161618f56",
            "Regular", "Marco Pedro", "925902123", "89")
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data1 = json.load(file)

        # Ahora creamos el mismo pero con familiar
        my_request1 = VaccineManager()
        my_request1.request_vaccination_id("6707dad0-c806-4901-87cf-d2e161618f56",
            "Familiar", "Marco Pedro", "925902123", "89")

        #Por último, comprobamos que el segundo tenga "Familiar"
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data2 = json.load(file)

        self.assertEqual(data1[0], data2[0])
        self.assertTrue(data2[1]['_VaccinePatientRegister__registration_type'] == "Familiar")

if __name__ == '__main__':
    unittest.main()
