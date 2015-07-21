import os

DEBUG = True
DEED_API_BASE_HOST = os.getenv('DEED_API_ADDRESS', '')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', '')
