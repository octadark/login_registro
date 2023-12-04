from flask import Flask
import re

app = Flask(__name__)
app.secret_key = "secretito"

BASE_DATOS = "db_login_registro"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')