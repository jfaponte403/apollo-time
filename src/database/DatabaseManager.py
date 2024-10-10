import logging
from sqlalchemy.schema import CreateTable
from sqlalchemy import MetaData, text
from sqlalchemy.orm import sessionmaker
from src.database.database import engine


logger = logging.getLogger(__name__)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db  
    finally:
        db.close() 
class DatabaseManager:
    def __init__(self):
        self.meta = MetaData()
        self.meta.reflect(bind=engine)

    def export_to_sql(self, filename='init.sql'):
        with open(filename, 'w') as f:
            for table in self.meta.sorted_tables:
                f.write(str(CreateTable(table)) + ";\n")
                logger.info(f"Created table statement for {table.name}.")

                with engine.connect() as connection:
                    results = connection.execute(table.select())
                    for row in results:
                        values = ', '.join(f"'{value}'" if isinstance(value, str) else str(value) for value in row)
                        insert_stmt = f"INSERT INTO {table.name} VALUES ({values});\n"
                        f.write(insert_stmt)
                        logger.info(f"Inserted row into {table.name}: {values}.")

    def import_from_sql(self, filename='init.sql'):
        with engine.connect() as connection:
            with connection.begin():
                for table in reversed(self.meta.sorted_tables):
                    logger.info(f"Deleting table {table.name}")
                    connection.execute(text(f"DROP TABLE IF EXISTS {table.name} CASCADE"))
                logger.info("All tables have been deleted.")

        with open(filename, "r") as file:
            sql_statements = file.read()

        with engine.connect() as connection:
            with connection.begin():
                for statement in sql_statements.split(";"):
                    if statement.strip():
                        connection.execute(text(statement.strip()))
                        logger.info(f"Executed statement: {statement.strip()[:50]}...")

                logger.info("The database has been updated.")


# Usage
if __name__ == '__main__':
    request = 0

    if request == 0:
        DatabaseManager().export_to_sql()

    if request == 1:
        DatabaseManager().import_from_sql()
