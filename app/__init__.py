# Author: Sakthi Santhosh
# Created on: 25/09/2023
from flask import Flask

from app.config import Config

app_handle = Flask(__name__)

app_handle.config.from_object(obj=Config)

import app.routes
