"""Module """
import re
class VaccineManager:
    """Class for providing the methods for managing the vaccination process"""
    def __init__(self):
        pass

    @staticmethod
    def validate_guid(patient_id):
        """RETURN TRUE IF THE GUID v4 IS RIGHT, OR FALSE IN OTHER CASE"""
        correct_id = r"[A-F0-9a-f]{8}-([0-9A-Fa-f]{4}-)" \
                     r"{2}[AB89ab89][A-F0-9a-f]{3}-[A-F0-9a-f]{12}"
        result = False
        if re.fullmatch(correct_id, patient_id):
            result = True
        return result