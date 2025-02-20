import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('host', 'localhost').strip("'")
user = os.getenv('user', 'admin').strip("'")
password = os.getenv('password', 'password').strip("'")
db = os.getenv('db', 'college').strip("'")

print(f'Attempting to connect with:\nhost: {host}\nuser: {user}\npassword: {password}\ndb: {db}')

try:
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=db,
        connect_timeout=5
    )
    print('Successfully connected to the database!')
    conn.close()
except pymysql.err.OperationalError as e:
    print(f'Connection failed: {e}')
except Exception as e:
    print(f'Unexpected error: {e}')