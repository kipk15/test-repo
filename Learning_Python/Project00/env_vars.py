import os

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')

print(os.environ.get('DB_USER'))
print(db_password)