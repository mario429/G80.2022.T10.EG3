# pylint: disable=R0904
# pylint: disable=R0913
# pylint: disable-msg=too-many-locals
# pylint: disable-msg=too-many-branches
# pylint: disable-msg=too-many-statements
"""

Module for the management of the vaccination process

"""
import re
import json
from datetime import datetime
from pathlib import Path
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

        Return True if the GUID v4 is right, or false in other case

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


    @staticmethod
    def validate_date_signature(patient_sys_id):
        """

        Returns True if the patient's date_signature is fully validated

        """
        # Check data type
        if not patient_sys_id or type(patient_sys_id) != str:
            raise VaccineManagementException("Error: invalid Patient's date_signature' --> Signature's data type is not String")

        # Check the length of the signature (must be exactly 64 bytes)
        patient_sys_id_length = len(patient_sys_id)
        if patient_sys_id_length != 64:
            raise VaccineManagementException("Error: invalid Patient's date_signature --> Signature must have 64 bytes")

        # Check the structure with regex
        valid_signature_regex = re.compile(r'[0-9a-f]{64}', re.IGNORECASE)
        check_signature = valid_signature_regex.fullmatch(patient_sys_id)
        if not check_signature:
            raise VaccineManagementException("Error: invalid Patient's date_signature' --> Signature does not match with regex")
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
        return new_client.get_patient_system_id()


    def get_vaccine_date(self, input_file):
        """

        DOCSTRING

        """
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"

        #Abrimos el fichero de entrada para comprobar los datos

        with open(input_file, "r", encoding="utf-8", newline="") as file:
            try:
                patient_data = json.load(file)
            except:
                raise VaccineManagementException("Wrong json file format")

        #############################COMPROBACIONES#############################

        if type(patient_data) != dict or len(patient_data.keys()) < 2:
            raise VaccineManagementException("Wrong json file format")
        dict_keys = list(patient_data.keys())
        if dict_keys[0] != "PatientSystemID" or dict_keys[1] != "ContactPhoneNumber":
            raise VaccineManagementException("Wrong json file format")

        good_id = re.compile(r"[0-9A-Fa-f]{32}")
        test_id = good_id.fullmatch(patient_data["PatientSystemID"])
        if not test_id:
            raise VaccineManagementException("Wrong json file format")


        good_number = re.compile(r"[0-9]{9}")
        test_number = good_number.fullmatch(patient_data["ContactPhoneNumber"])
        if not test_number:
            raise VaccineManagementException("Wrong json file format")

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

        #Comprobamos que el cliente no tiene ya una cita

        file_store_date = json_path + "store_patient_date.json"

        try:
            with open(file_store_date, 'r', encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            data_list = []
        except json.JSONDecodeError:
            raise VaccineManagementException("JSON Decode Error - Wrong JSON Format")
        found = False
        for item in data_list:
            if item["_VaccinationAppoinment__patient_sys_id"] == client_system_id:
                found = True
        if found:
            raise VaccineManagementException("Error: patient already has an appointment.")
        ##################################################

        #Se le añade al fichero
        data_list.append(new_date.__dict__)
        try:
            with open(file_store_date, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except:
            raise VaccineManagementException("Wrong file or path")
        print(data_list)
        return new_date.vaccination_signature


    def vaccine_patient(self, date_signature):
        """

        Method that validates and searches a patient given a date_signature

        """
        # First we need to validate the date_signature argument
        self.validate_date_signature(date_signature)

        # Then we need to check if date_signature exists in store_patient_date
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store_date = json_path + "store_patient_date.json"

        # We check if there are any file errors

        try:
            with open(file_store_date, 'r', encoding="utf-8", newline="") as file:
                data_list = json.load(file)

        except FileNotFoundError:
            data_list = []

        except json.JSONDecodeError:
            raise VaccineManagementException("JSON Decode Error - Wrong JSON Format")

        # Now we traverse the JSON file searching for the date_signature

        date_founded = False
        for item in data_list:
            if item["_VaccinationAppoinment__date_signature"] == date_signature:
                date_founded = True
                appointment_date = item["_VaccinationAppoinment__appoinment_date"]
        if not date_founded:
            raise VaccineManagementException("Error: date_signature doesn't exist in the system")

        # If we found date_signature in the JSON file the we need to check if the vaccination date is today

        actual_date = datetime.timestamp(datetime.utcnow())
        # print(appointment_date)
        # print(actual_date)
        print(actual_date)
        print(appointment_date)
        if actual_date != appointment_date:
            raise VaccineManagementException("Error: actual date doesn't match with the issued vaccination date")

        # At this point, if the issued_date is equal to actual_date, the system creates a new store with the vaccination data

        try:
            with open(str(json_path+"store_vaccine_patient.json"), "w", encoding="utf-8", newline="") as file:
                json.dump([{str(date_signature): actual_date}], file, indent=2)
        except:
            raise VaccineManagementException("Wrong file or path")
        return True
