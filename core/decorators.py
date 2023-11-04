import functools
from inspect import signature
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)
HANDLER = logging.StreamHandler()
LOGGER.addHandler(HANDLER)


def logger(func):
    parameters = list(signature(func).parameters.keys())
    if "self" in parameters:
        function_type = "METHOD"
    elif "cls" in parameters:
        function_type = "CLASS_METHOD"
    else:
        function_type = "FUNCTION"

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if function_type == "METHOD":
            function_name = f"{args[0].__class__.__name__}.{func.__name__}"
        elif function_type == "CLASS_METHOD":
            function_name = f"{args[0].__name__}.{func.__name__}"
        else:
            function_name = func.__name__
        LOGGER.info(f"Calling {function_name} with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        LOGGER.info(f"{function_name} execution complete. Returned value: {result}")
        return result
    return wrapper
