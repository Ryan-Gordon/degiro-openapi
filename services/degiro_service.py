import degiroapi
class DegiroService(object):
    def login(self, request_body):
        try:
            degiro = degiroapi.DeGiro()
            resp = degiro.login(request_body.get("username"), request_body.get("password"))
            return resp
        except Exception as exc:
            return str(exc), 401
