import degiroapi
import connexion
from base64 import b64decode, b64encode

class DegiroService(object):
    def login(self, request_body):
        try:
            degiro = degiroapi.DeGiro()
            resp = degiro.login(request_body.get("username"), request_body.get("password"))
            return resp
        except Exception as exc:
            return str(exc), 401

    def get_cash_funds(self):
        try:
            degiro = degiroapi.DeGiro()
            resp = degiro.login(*self.parse_basic_auth_creds())
            cachfunds = degiro.getdata(degiroapi.Data.Type.CASHFUNDS)
            return cachfunds, 200
        except Exception as exc:
            return str(exc), 401

    def parse_basic_auth_creds(self):
        split = connexion.request.headers["Authorization"].split(' ')
        if split[0].strip().lower() == 'basic':
            try:
                username, password = b64decode(split[1]).decode().split(':', 1)
            except:
                raise DecodeError
        else:
          raise DecodeError
        return username, password
