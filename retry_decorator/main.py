from functools import wraps
from retrying import retry, RetryError
import random

# Decorator para hacer retrys
def printing_retry(*args, **kwargs):
    def decorator(f):
        decorated = retry(*args, **kwargs)(f)

        @wraps(decorated)
        def wrapper(*args, **kwargs):
            try:
                return decorated(*args, **kwargs)
            except RetryError:
                raise RetryError("Maximo reintento de conecciones excedido")

        return wrapper

    if len(args) == 1 and callable(args[0]):
        return decorator(args[0])
    return decorator


@printing_retry(stop_max_attempt_number=1, wrap_exception=True)
def conectar():
    if random.randint(0, 10) > 1:
        raise IOError("Error al conectar!!!")
    else:
        return "Conectado!"


print(conectar())
