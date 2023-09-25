# Author: Sakthi Santhosh
# Created on: 25/09/2023
from secrets import token_hex

class Config:
    SECRET_TOKEN = token_hex(8)
