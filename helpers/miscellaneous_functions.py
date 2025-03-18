import os

def get_env_var(var_name: str) -> str:
    val = os.getenv(var_name)

    if val is None:
        raise Exception(f'Environment variable {var_name} is not set')

    return val


def get_base_route():
    return get_env_var('BASE_ROUTE')
