class EmergencyHistory:
    def __init__(self, presenting_complaint, socrates):
        self.presenting_complaint = presenting_complaint
        self.socrates = {
            "site": None,
            "onset": None,
            "character": None,
            "radiation": None,
            "associations": None,
            "timing": None,
            "alleviation": None,
            "exacerbation": None,
            "sleep": None,
            "severity": None
        }