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
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()