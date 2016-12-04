from tastypie.api import Api
from cuber.settings import API_NAME
from taxi.api import CarResource
from travels.api import TravelRequestResource

v1_api = Api(api_name=API_NAME)
v1_api.register(CarResource())
v1_api.register(TravelRequestResource())
