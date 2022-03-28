from functools import wraps

# Run unit tests with "python -m unittest discover --pattern '*_test.py' --failfast --quiet"
def describe(description: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            raw_test_name = f'{func.__name__}'.replace('test_', '')
            module_name = f'{func.__module__}'.split('.')[-1]

            print(f'Running {raw_test_name} on {module_name}')
            print(f'{description}\n')

            return func(*args, **kwargs)

        return wrapper

    return decorator
