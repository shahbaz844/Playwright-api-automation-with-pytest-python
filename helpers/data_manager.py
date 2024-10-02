class DataManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._data = {}
        self._initialized = True

    @classmethod
    def get_instance(cls):
        return cls.__new__(cls)

    def set_data(self, key, value):
        self._data[key] = value

    def get_data(self, key):
        return self._data.get(key)
