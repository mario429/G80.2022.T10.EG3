"""Module """
import uuid
import re
from vaccine_management_exception import VaccineManagementException
class VaccineManager:
    """Class for providing the methods for managing the vaccination process"""
    def __init__(self):
        pass

    @staticmethod
    def validate_guid(patient_id):
        """RETURN TRUE IF THE GUID v4 IS RIGHT, OR FALSE IN OTHER CASE"""
        try:
            my_r = re.compile (r'^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-'
                               r'[0-9A-F]{12}$', re.IGNORECASE)
            this_r = my_r.fullmatch(patient_id)
            if not this_r:
                raise VaccineManagementException("Error: invalid UUID version")
        except ValueError:
            raise VaccineManagementException("Error: invalid UUID")
        return True

    def request_vaccination_id (self, patient_id, registration_type, name_surname, phone_number, age):
        #Primero manejamos los errores con patient_id
        if not patient_id:
            raise VaccineManagementException ("Error: please enter a UUID")
        if (type(patient_id) != str):
            raise VaccineManagementException ("Error: UUID must be a string")
        self.validate_guid(patient_id) #Se encarga de ver si patient_id es un UUID v4 válido

        #Errores con registration_type

        if not registration_type:
            raise VaccineManagementException("Error: registration type can't be null")
        if (type(registration_type) != str):
            raise VaccineManagementException("Error: registration type must be a string")
        if (registration_type != "Familiar" and registration_type != "Regular"):
            raise VaccineManagementException("Error: invalid registration type")

        #Errores con name_surname

        if not name_surname:
            raise VaccineManagementException("Error: name can't be null")
        if type(name_surname) != str:
            raise VaccineManagementException("Error: name must be a string")
        if len(name_surname) > 30:
            raise VaccineManagementException("Error: name is too long")

        test_arr = name_surname.split()

        if len(test_arr) != 2:
            raise VaccineManagementException("Error: name must have two words, separated by a space and contain no digits")
        acceptable=["á", "é", "í", "ó", "ú", "ñ", "ç"]
        for i in name_surname:
            if not i.isalpha() and i not in acceptable and i!= " ":
                raise VaccineManagementException(
                    "Error: name must have two words, separated by a space and contain no digits")


        #Errores con phone_number




