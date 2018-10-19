from hackathon import app
from flask_restplus import Api, Resource

from hackathon.loader import resource_load

from flask import url_for
from flask_cors import CORS

app.config['ERROR_INCLUDE_MESSAGE'] = False

CORS(app)


@property
def specs_url(self):
    return url_for(self.endpoint('specs'), _external=True, _scheme='https')


# Only for production mode
if app.debug is False:
    Api.specs_url = specs_url

api = Api(
    app,
    title='hackathon API',
    version='1.0',
    description="hackathon"
)

resource_load(
    'test'
)
