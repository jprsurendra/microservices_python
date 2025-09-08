from threading import Lock

class ThreadSafeSingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class PaymentsData(metaclass=ThreadSafeSingletonMeta):
    def __init__(self):
        super().__init__()
        # Fake orders
        self.payment = {
            "501": {"order_id": "101", "amount": 1200},
            "502": {"order_id": "102", "amount": 800}
        }

    def get_payment(self, payment_id):
        return self.payment.get(payment_id)
