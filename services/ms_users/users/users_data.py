from threading import Lock

class ThreadSafeSingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class UsersData(metaclass=ThreadSafeSingletonMeta):
    def __init__(self):
        super().__init__()
        self.users = {   "1": "Alice",
                         "2": "Bob",
                         "3": "Charlie" }

    def get_user(self, user_id):
        return self.users.get(user_id, "Unknown")
