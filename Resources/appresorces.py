def print_C(text):
    print(text)


def input_C(text):
    input_value = input(text)
    return input_value


def IsPythonFilename(file_name):
    suffix = file_name[-len(".py"):]
    if suffix == ".py":
        return True
    return False

class Exit(Exception):
    """
    Exception for exit from program
    """
    pass

def Command(name, docs=None):
    def decorator(func):
        CommandsConfig[name.lower()] = {'func': func, 'docs': docs}
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

CommandsConfig = {}