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
            raise VaccineManagementException("Error: invalid Patient's date_signature' "
                "--> Signature's data type is not String")

        # Check the length of the signature (must be exactly 64 bytes)
        patient_sys_id_length = len(patient_sys_id)
        if patient_sys_id_length != 64:
            raise VaccineManagementException("Error: invalid Patient's date_signature "
                "--> Signature must have 64 bytes")

        # Check the structure with regex
        valid_signature_regex = re.compile(r'[0-9a-f]{64}', re.IGNORECASE)
        check_signature = valid_signature_regex.fullmatch(patient_sys_id)
        if not check_signature:
            raise VaccineManagementException("Error: invalid Patient's date_signature' "
                "--> Signature does not match with regex")
        return True


    def request_vaccination_id(self, patient_id, registration_type,
        name_surname, phone_number, age):
        """

        Method that validates a patient's data for vaccination

        """

        # First we deal with errors related to patient_id
        if not patient_id or type(patient_id) != str:
            raise VaccineManagementException("Error: invalid UUID")

        # It checks if patient_id is a valid UUID v4
        # If there are no errors, continue with the execution
        self.validate_guid(patient_id)

        # registration_type errors
        if registration_type != "Regular" and registration_type != "Familiar":
            raise VaccineManagementException("Error: registration_type must be "
                "'Familiar' or 'Regular'")

        # name_surname errors
        if not name_surname or type(name_surname) != str:
            raise VaccineManagementException("Error: wrong name format")
        if len(name_surname) > 30:
            raise VaccineManagementException("Error: name is too long")

        # Checks if it suits the regex "formula"
        good_name = re.compile(r'\w+\s\w+')
        test_name = good_name.fullmatch(name_surname)
        if not test_name:
            raise VaccineManagementException("Error: wrong name format")

        # phone_number errors
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

        # age errors
        if not age or type(age) != str:
            raise VaccineManagementException("Error: invalid age format")
        good_age = re.compile(r"^\d+$")# Age has only two numbers
        test_age = good_age.fullmatch(age)
        if not test_age:
            raise VaccineManagementException("Error: invalid age format")
        if int(age) not in range (6, 126):
            raise VaccineManagementException("Error: age must be between 6 and 125")

        new_client = VaccinePatientRegister(patient_id, name_surname,
            registration_type, phone_number, age)

        # Checks if the patient is already registered in the system
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

        # If we reach here, the patient is not in the system, so we add him
        data_list.append(new_client.__dict__)
        try:
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except:
            raise VaccineManagementException("Wrong file or path")
        return new_client.get_patient_system_id()


    def get_vaccine_date(self, input_file):
        """

        Method that returns a 64-byte hash of the date

        """
        json_path = str(Path.home()) + "/PycharmProjects/G80.2022.T10.EG3/src/JsonFiles/"
        file_store = json_path + "store_patient.json"

        # We open the input file to check the data

        with open(input_file, "r", encoding="utf-8", newline="") as file:
            try:
                patient_data = json.load(file)
            except:
                raise VaccineManagementException("Wrong json file format")

        #############################CHECKS#############################

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

        # Opens the file that contains the patients to check if it finds the value
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)

        client_system_id = patient_data["PatientSystemID"]
        client_phone_number = patient_data["ContactPhoneNumber"]

        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_sys_id"] == \
                client_system_id and item['_VaccinePatientRegister__phone_number'] == \
                    client_phone_number:
                found = True
                guid = item['_VaccinePatientRegister__patient_id']
                break
        if not found:
            raise VaccineManagementException("Patient does not exist")

        # It has been found, so we create an instance of VaccinationAppointment
        new_date = VaccinationAppoinment(guid, client_system_id, client_phone_number, 10)

        # Checks if the client hasn't got an appointment already
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

        # Adding the data to the file
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

        # If signature is valid and exists in store_patient_date we check if it already
        # exists in store_vaccine_patient
        try:
            with open(str(json_path)+"store_vaccine_patient.json", 'r',
                    encoding='utf-8', newline="") as file:
                vaccine_patients = json.load(file)[0]
                if vaccine_patients[date_signature]:
                    raise VaccineManagementException("Error: Patient has already been vaccinated")
        except FileNotFoundError:
            pass

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

        # If we found date_signature in the JSON file the we
        # need to check if the vaccination date is today
        actual_date = datetime.timestamp(datetime.utcnow())
        if actual_date != appointment_date:
            raise VaccineManagementException("Error: actual date doesn't match with "
                "the issued vaccination date")

        # At this point, if the issued_date is equal to actual_date,
        # the system creates a new store with the vaccination data
        try:
            with open(str(json_path+"store_vaccine_patient.json"), "w",
                    encoding="utf-8", newline="") as file:
                json.dump([{str(date_signature): actual_date}], file, indent=2)
        except:
            raise VaccineManagementException("Wrong file or path")
        return True
