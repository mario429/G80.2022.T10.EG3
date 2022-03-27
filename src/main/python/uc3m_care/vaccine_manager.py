# pylint: disable=R0904
# pylint: disable=R0913
# pylint: disable-msg=too-many-locals
# pylint: disable-msg=too-many-branches
# pylint: disable-msg=too-many-statements
"""

Module for the management of the vaccination process

"""
import re
from pathlib import Path
import json
from .vaccine_management_exception import VaccineManagementException
from .vaccine_patient_register import VaccinePatientRegister
from .vaccination_appoinment import VaccinationAppoinment

class VaccineManager:
    """

    Class for providing the methods for managing the vaccination process

    """
    def __init__(self):
        """

        Constructor (with pass function)

        """

    @staticmethod
    def validate_guid(patient_id):
        """

        RETURN TRUE IF THE GUID v4 IS RIGHT, OR FALSE IN OTHER CASE

        """
        valid_guid = re.compile (r'^[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-'
                                 r'[0-9A-F]{12}$', re.IGNORECASE)
        valid_guid4 = re.compile(r'^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-'
                          r'[0-9A-F]{12}$', re.IGNORECASE)
        check_guid = valid_guid.fullmatch(patient_id)
        check_guid_version = valid_guid4.fullmatch(patient_id)
        if not check_guid:
            raise VaccineManagementException("Error: invalid UUID")
        if not check_guid_version:
            raise VaccineManagementException("Error: invalid UUID version")
        return True

    def request_vaccination_id(self, patient_id, registration_type,
        name_surname, phone_number, age):
        """

        Method that validates a patient's data for vaccination

        """

        # Primero manejamos los errores con patient_id
        if not patient_id or type(patient_id) != str:
            raise VaccineManagementException("Error: invalid UUID")

        # Se encarga de ver si patient_id es un UUID v4 válido.
        # Si no hay errores, continúa la ejecución
        self.validate_guid(patient_id)

        # Errores con registration_type
        if registration_type != "Regular" and registration_type != "Familiar":
            raise VaccineManagementException("Error: registration_type must be "
                "'Familiar' or 'Regular'")

        # Errores con name_surname
        if not name_surname or type(name_surname) != str:
            raise VaccineManagementException("Error: wrong name format")
        if len(name_surname) > 30:
            raise VaccineManagementException("Error: name is too long")

        # Comprobamos si cumple la regex con dos palabras separadas por un espacio
        good_name = re.compile(r'\w+\s\w+')
        test_name = good_name.fullmatch(name_surname)
        if not test_name:
            raise VaccineManagementException("Error: wrong name format")

        acceptable = ["á", "é", "í", "ó", "ú", "ñ", "ç", "Á", "É", "Í", "Ó", "Ú", "ü"]

        # Comprobamos si hay caracteres no válidos
        for i in name_surname:
            if not i.isalpha() and i not in acceptable and i!= " ":
                raise VaccineManagementException("Error: wrong name format")

        # Errores con phone_number
        if not phone_number or type(phone_number) != str:
            raise VaccineManagementException("Error: invalid phone number format")
        if len(phone_number) != 9:
            raise VaccineManagementException("Error: number must contain "
                "9 characters and only digits")
        good_number = re.compile(r"[0-9]{9}")
        test_number = good_number.fullmatch(phone_number)
        if not test_number:
            raise VaccineManagementException("Error: number must contain "
                "9 characters and only numerals")

        # Errores con age
        if not age or type(age) != str:
            raise VaccineManagementException("Error: invalid age format")
        good_age = re.compile(r"^\d+$")# Age solo tiene números
        test_age = good_age.fullmatch(age)
        if not test_age:
            raise VaccineManagementException("Error: invalid age format")
        if int(age) not in range (6, 126):
            raise VaccineManagementException("Error: age must be between 6 and 125")

        new_client = VaccinePatientRegister(patient_id, name_surname,
            registration_type, phone_number, age)

        # Vemos si el paciente ya está en el sistema
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"

        try:
            with open(file_store, 'r', encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            data_list = []
        except json.JSONDecodeError:
            raise VaccineManagementException("JSON Decode Error - Wrong JSON Format")
        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == patient_id:
                if (item["_VaccinePatientRegister__registration_type"] == \
                    registration_type) and (item["_VaccinePatientRegister__full_name"] ==
                        name_surname):
                    found = True
        if found:
            raise VaccineManagementException("Error: patient ID already registered")

        # Si estamos aquí, el paciente no se encuentra en el sistema, así que lo añadimos
        data_list.append(new_client.__dict__)
        try:
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except:
            raise VaccineManagementException("Wrong file or path")
        return new_client.patient_system_id

    def get_vaccine_date(self, input_file):

        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"
        #Abrimos el fichero de entrada para comprobar los datos

        with open(input_file, "r", encoding="utf-8", newline="") as file:
            patient_data = json.load(file)
        #############################COMPROBACIONES##################################################

        #Abrimos el fichero que guarda los pacientes para ver si se encuentra el valor
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)

        client_system_id = patient_data["PatientSystemID"]
        client_phone_number = patient_data["ContactPhoneNumber"]


        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_sys_id"] == client_system_id and item['_VaccinePatientRegister__phone_number'] == client_phone_number:
                found = True
                guid = item['_VaccinePatientRegister__patient_id']
                break
        if not found:
            raise VaccineManagementException("Patient does not exist")

        #Como se ha encontrado, se crea instancia de VaccinationAppointment

        new_date = VaccinationAppoinment(guid, client_system_id, client_phone_number, 10)

        return new_date.vaccination_signature



