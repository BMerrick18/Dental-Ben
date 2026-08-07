class Examination:
    def __init__(self, extra_oral, intra_oral_st, intra_oral_ht, special_tests):
        self.extra_oral = {
            "lymph nodes": None,
            "salivary glands": None,
            "submandibular zone": None,
            "neck": None,
            "tmj": None,
        }
        self.intra_oral_st = {
            "palate": None,
            "cheeks": None,
            "lips": None,
            "tongue": None,
            "gingiva": None,
            "floor of mouth": None,
        }
        self.intra_oral_ht = {
            "caries": None,
            "retained roots": None,
            "fractures": None,
            "recurrent caries": None,
        }
        self.special_tests = {
            "ttp": None,
            "endofrost": None,
        }