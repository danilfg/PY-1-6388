# Single instance class (beginner level)
class DatabaseSingleton:
    _instance = None
    _config: dict

    @classmethod
    def instance(cls, config_dict: dict = {}):
        if cls._instance is None:
            cls._instance = DatabaseSingleton(config_dict)

        return cls._instance

    def __init__(self, config_dict: dict):
        self._config = config_dict


CONFIG = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "root",
    "database": "dev"
}

db = DatabaseSingleton.instance(CONFIG)
# db.set_config()
print(db._config)
db2 = DatabaseSingleton.instance()
print(db2._config)
# db3 = DatabaseSingleton()  # not singleton
