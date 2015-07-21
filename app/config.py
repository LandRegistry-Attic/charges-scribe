import os

DEBUG = True
DEED_API_BASE_HOST = os.getenv('DEED_API_ADDRESS', 'http://10.10.10.10:5000')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', '')
