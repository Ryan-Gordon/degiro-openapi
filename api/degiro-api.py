from flask_injector import inject
from services.degiro_service import DegiroService
import flask

from flask import request, Response

'''

'''
@inject(data_provider=DegiroService)
def login(data_provider, body) -> str:
    return data_provider.login(body)


