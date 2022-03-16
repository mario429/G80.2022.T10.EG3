import unittest
from uc3m_care import VaccineManager
from uc3m_care import VaccineManagementException

class MyTestCase(unittest.TestCase):
    def test1_request_vaccination_ok(self):
        my_request = VaccineManager()

        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                  "Jose Johnson", "923412921", "45")
        self.assertEqual("8bc92caa91fccc9370222915038ab642", value)

    def test2_request_vaccination_notok_uuid1(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-113f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", "923412921", "45")
        self.assertEqual("Error: invalid UUID version", cm.exception.message)

    def test3_request_vaccination_notok_uuid2(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("zbb5dbd6f-d8b4-113f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", "923412921", "45")
        self.assertEqual("Error: invalid UUID", cm.exception.message)

    def test4_request_vaccination_notok_uuid2(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("gghg", "Regular",
                                                      "Jose Johnson", "923412921", "45")
        self.assertEqual("Error: invalid UUID", cm.exception.message)

    def test5_request_vaccination_notok_uuid3(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id(None, "Regular",
                                                      "Jose Johnson", "923412921", "45")
        self.assertEqual("Error: please enter a UUID", cm.exception.message)

    def test6_request_vaccination_notok_uuid4(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id(99999, "Regular",
                                                      "Jose Johnson", "923412921", "45")
        self.assertEqual("Error: UUID must be a string", cm.exception.message)

    def test7_request_vaccination_ok(self):
        my_request = VaccineManager()

        value = my_request.request_vaccination_id("567f65de-5c03-4e8e-ae50-aa6b49b6893f", "Familiar",
                                                  "Alfredo Sánchez", "666111222", "12")
        self.assertEqual("ec5a2ec5753f1cdee94cc24e858ab6b4", value)

    def test8_request_vaccination_ok(self):
        my_request = VaccineManager()

        value = my_request.request_vaccination_id("eb6cb027-08e9-4d11-bc85-dabf844bae22", "Familiar",
                                                  "Pedro Son", "552555222", "56")
        self.assertEqual("a1ee58f3fedef5dc284523b0c96a21ca", value)

    def test9_request_vaccination_notok_reg1(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Perros",
                                                          "Toby Woof", "923412921", "8")
        self.assertEqual("Error: invalid registration type", cm.exception.message)

    def test10_request_vaccination_notok_reg1(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "p231m2",
                                                          "Toby Woof", "923412921", "8")
        self.assertEqual("Error: invalid registration type", cm.exception.message)

    def test11_request_vaccination_notok_reg2(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", 234231,
                                                          "Toby Woof", "923412921", "8")
        self.assertEqual("Error: registration type must be a string", cm.exception.message)

    def test12_request_vaccination_notok_reg2(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", 231.123,
                                                          "Toby Woof", "923412921", "8")
        self.assertEqual("Error: registration type must be a string", cm.exception.message)

    def test13_request_vaccination_notok_reg3(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", None,
                                                          "Toby Woof", "923412921", "8")
        self.assertEqual("Error: registration type can't be null", cm.exception.message)

    def test14_request_vaccination_notok_name1(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                          "Jose Federicogonzaloramonperecianorodríguez", "923412921", "45")
        self.assertEqual("Error: name is too long", cm.exception.message)

    def test15_request_vaccination_notok_name2(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                          "Juan Nepomuceno96", "923412921", "45")
        self.assertEqual("Error: name must have two words, separated by a space and contain no digits", cm.exception.message)

    def test16_request_vaccination_notok_name2(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                          "198Juan Nepomuceno", "923412921", "45")
        self.assertEqual("Error: name must have two words, separated by a space and contain no digits", cm.exception.message)

    def test17_request_vaccination_notok_name3(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                          "Feliciano", "923412921", "45")
        self.assertEqual("Error: name must have two words, separated by a space and contain no digits", cm.exception.message)

    def test18_request_vaccination_notok_name4(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                          "Pepe González de la Santa Sal", "923412921", "45")
        self.assertEqual("Error: name must have two words, separated by a space and contain no digits", cm.exception.message)

    def test19_request_vaccination_notok_name4(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                          "Nombre muy Incorrecto", "923412921", "45")
        self.assertEqual("Error: name must have two words, separated by a space and contain no digits", cm.exception.message)

    def test20_request_vaccination_notok_name5(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                          2341231, "923412921", "45")
        self.assertEqual("Error: name must be a string", cm.exception.message)

    def test21_request_vaccination_notok_number1(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", "99123", "45")
        self.assertEqual("Error: number must contain 9 characters and only numerals", cm.exception.message)

    def test22_request_vaccination_notok_number1(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", "0", "45")
        self.assertEqual("Error: number must contain 9 characters and only numerals", cm.exception.message)

    def test23_request_vaccination_notok_number1(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", "", "45")
        self.assertEqual("Error: no phone number", cm.exception.message)

    def test24_request_vaccination_notok_number2(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", "23424534324", "45")
        self.assertEqual("Error: number must contain 9 characters and only numerals", cm.exception.message)

    def test25_request_vaccination_notok_number3(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", "Esteesmino", "45")
        self.assertEqual("Error: number must contain 9 characters and only numerals", cm.exception.message)

    def test26_request_vaccination_notok_number3(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", "234num2323", "45")
        self.assertEqual("Error: number must contain 9 characters and only numerals", cm.exception.message)

    def test27_request_vaccination_notok_number4(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", None, "45")
        self.assertEqual("Error: no phone number", cm.exception.message)

    def test28_request_vaccination_notok_number5(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", 24.67, "45")
        self.assertEqual("Error: number must be a string", cm.exception.message)

    def test29_request_vaccination_notok_age1(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", "685838390", "5")
        self.assertEqual("Error: age must be between 6 and 125", cm.exception.message)

    def test30_request_vaccination_notok_age1(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", "685838390", "-3241")
        self.assertEqual("Error: age string must only contain a number from 6 to 125", cm.exception.message)

    def test31_request_vaccination_notok_age2(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", "685838390", "126")
        self.assertEqual("Error: age must be between 6 and 125", cm.exception.message)

    def test32_request_vaccination_notok_age2(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", "685838390", "9999")
        self.assertEqual("Error: age must be between 6 and 125", cm.exception.message)

    def test33_request_vaccination_notok_age2(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", "685838390", "64.35")
        self.assertEqual("Error: age string must only contain a number from 6 to 125", cm.exception.message)

    def test34_request_vaccination_notok_age2(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", "685838390", "32.00")
        self.assertEqual("Error: age string must only contain a number from 6 to 125", cm.exception.message)

    def test35_request_vaccination_notok_age3(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                      "Jose Johnson", "685838390", "stringnum")
        self.assertEqual("Error: age string must only contain a number from 6 to 125", cm.exception.message)

    def test36_request_vaccination_ok(self):
        my_request = VaccineManager()

        value = my_request.request_vaccination_id("cb3dd087-0868-4203-bbbd-5e7899fbbe2a", "Regular",
                                                  "Rosa García", "678923456", "34")
        self.assertEqual("4a1972fa6d088c1a119cf65cf9039f88", value)

    def test37_request_vaccination_notok_uuid4(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id(None, "Regular",
                                                      "Jose Johnson", "923412921", "45")
        self.assertEqual("Error: please enter a UUID", cm.exception.message)

    def test38_request_vaccination_notok_name6(self):
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                                          None, "923412921", "45")
        self.assertEqual("Error: name can't be null", cm.exception.message)









if __name__ == '__main__':
    unittest.main()
