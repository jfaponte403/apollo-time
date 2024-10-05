import os
import logging
from sqlalchemy import create_engine, exc
from src.utils.EnvironmentVariableResolver import EnvironmentVariableResolver

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
env_resolver = EnvironmentVariableResolver()

POSTGRES_USER = env_resolver.get_postgres_user()
POSTGRES_PASSWORD = env_resolver.get_postgres_password()
POSTGRES_HOST = env_resolver.get_postgres_host()
POSTGRES_PORT = env_resolver.get_postgres_port()
POSTGRES_DB = env_resolver.get_postgres_db()

missing_vars = []
if not POSTGRES_USER:
    missing_vars.append("POSTGRES_USER")
if not POSTGRES_PASSWORD:
    missing_vars.append("POSTGRES_PASSWORD")
if not POSTGRES_HOST:
    missing_vars.append("POSTGRES_HOST")
if not POSTGRES_PORT:
    missing_vars.append("POSTGRES_PORT")
if not POSTGRES_DB:
    missing_vars.append("POSTGRES_DB")

if missing_vars:
    logger.error(f"Missing environment variables: {', '.join(missing_vars)}")
    raise ValueError("Please ensure that all environment variables are set correctly.")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
try:
    logger.info("Creating the database engine...")
    engine = create_engine(DATABASE_URL)

    with engine.connect() as connection:
        logger.info("Connection to the database was successful!")
except exc.SQLAlchemyError as e:
    logger.error(f"An error occurred while connecting to the database: {e}")
    raise
except Exception as e:
    logger.error(f"An unexpected error occurred: {e}")
    raise
