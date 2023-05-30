import os

PROJECT_NAME = "devi-revolutti"
VERSION = "0.1.0"
DATABASE_HOST: str = os.getenv('DATABASE_HOST', f"127.0.0.1")
DATABASE_PORT: str = os.getenv('DATABASE_PORT', f"3306")
DATABASE_USER: str = os.getenv('DATABASE_USER', f"root")
DATABASE_PASS: str = os.getenv('DATABASE_PASS', f"")
DATABASE_NAME: str = os.getenv('DATABASE_NAME', f"db")
SQLALCHEMY_DATABASE_URL: str = os.getenv('DATABASE_URI',
                                         "mysql+mysqlconnector://{username}:{password}@{host}:{port}/{name}".format(
                                             username=DATABASE_USER, password=DATABASE_PASS, host=DATABASE_HOST,
                                             port=DATABASE_PORT, name=DATABASE_NAME))

DEBUG = True
