import os
from dotenv import load_dotenv

class EnvironmentVariableResolver:

    def __init__(self):
        load_dotenv(dotenv_path=os.path.join('src', '.env'))
        self._environment_variables = os.environ

    def get_postgres_user(self) -> str:
        return self._environment_variables['POSTGRES_USER']

    def get_postgres_password(self) -> str:
        return self._environment_variables['POSTGRES_PASSWORD']

    def get_postgres_host(self) -> str:
        return self._environment_variables['POSTGRES_HOST']

    def get_postgres_port(self) -> str:
        return self._environment_variables['POSTGRES_PORT']

    def get_postgres_db(self) -> str:
        return self._environment_variables['POSTGRES_DB']

    def get_secret_key(self) -> str:
        return self._environment_variables['SECRET_KEY']

    def get_algorithm(self) -> str:
        return self._environment_variables['ALGORITHM']

    def get_access_token_expire_minutes(self) -> int:
        return int(self._environment_variables['ACCESS_TOKEN_EXPIRE_MINUTES'])

    def get_postgres_test(self) -> str:
        return self._environment_variables['TEST']
