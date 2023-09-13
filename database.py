class Database:
    @classmethod
    def get_instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = Database()
        return cls._instance

    def __init__(self):
        self.tolls = {}
        self.booths = {}
        self.charges = {}
        self.passes = {}
