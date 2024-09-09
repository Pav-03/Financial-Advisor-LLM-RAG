from threading import Lock

class SingletonMeta(type):

    """
    This is a tread-safe implementation od Singleton
    """
    _instances = {}

    _lock: Lock = Lock()

    """
    we now have a lock object that will be used to syncronize thread during first access to the Singlton
    """

    def __call__(cls,*args, **kwargs):
        with cls._lock:
            if cls not in cls.instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]