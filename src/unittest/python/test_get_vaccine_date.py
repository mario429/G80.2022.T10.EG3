"""

DOCSTRING

"""
import unittest
import os
import json
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
        file_test = json_path + "tests_get_vaccine_date/test1_get_vaccine_date_ok.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        my_request = VaccineManager()
        this_id = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0", "Regular",
                                          "Jose Johnson", "923412921", "45")

        value = my_request.get_vaccine_date(file_test)
        self.assertEqual(value, "f96386153f2767f620e5bacdf1d33b278fabe54bf4d43e7acb172233131de254")


if __name__ == '__main__':
    unittest.main()