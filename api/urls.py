from tastypie.api import Api
from cuber.settings import API_NAME
from taxi.api import CarResource

v1_api = Api(api_name=API_NAME)
v1_api.register(CarResource())
