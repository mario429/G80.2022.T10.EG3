"""Module """
import uuid
from vaccine_management_exception import VaccineManagementException
class VaccineManager:
    """Class for providing the methods for managing the vaccination process"""
    def __init__(self):
        pass

    @staticmethod
    def validate_guid(patient_id):
        """RETURN TRUE IF THE GUID v4 IS RIGHT, OR FALSE IN OTHER CASE"""
        try:
            myUUID = uuid.UUID (patient_id)
            import re
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


