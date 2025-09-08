from threading import Lock

class ThreadSafeSingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class OrdersData(metaclass=ThreadSafeSingletonMeta):
    def __init__(self):
        super().__init__()
        # Fake orders
        self.orders = {"101": {"user_id": "1", "item": "Laptop"},
                  "102": {"user_id": "2", "item": "Phone"}}

    def get_order(self, order_id):
        return self.orders.get(order_id, "Unknown")
