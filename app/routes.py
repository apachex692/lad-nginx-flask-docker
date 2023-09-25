# Author: Sakthi Santhosh
# Created on: 25/09/2023
from flask import render_template

from app import app_handle

@app_handle.route('/')
def index_handle():
    return render_template("index.html")
