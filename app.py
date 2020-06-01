import os
from injector import Binder
from flask_injector import FlaskInjector
from services.degiro_service import DegiroService
import connexion
from connexion.resolver import RestyResolver
import logging

from connexion.decorators.security import validate_scope
from connexion.exceptions import OAuthScopeProblem

# Set up logger
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def basic_auth(username, password, required_scopes=None):

    # optional
    if required_scopes is not None and not validate_scope(required_scopes, info['scope']):
        raise OAuthScopeProblem(
                description='Provided user doesn\'t have the required access rights',
                required_scopes=required_scopes,
                token_scopes=info['scope']
            )

    return {"sub":username, "secret":password}

def configure(binder: Binder) -> Binder:
    binder.bind(
        DegiroService, to=DegiroService()
    )

#Redefine application as a connexion app. 
application = connexion.App(__name__, specification_dir='openapi/')

# Setup RestyResolver and the OpenAPI docs
application.add_api('degiro-openapi.yaml', resolver=RestyResolver('api'), arguments={'title': 'Degiro OpenAPI'})

#FlaskInjector Setup defined after configure
FlaskInjector(app=application.app, modules=[configure])



if __name__ == '__main__':
    
    #Start the flask server on either a predefined port from the host machine or 2025
    application.run(debug=False, \
        #server='tornado', 
        port=int(os.environ.get('PORT', 2025)))