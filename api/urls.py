from tastypie.api import Api
from cuber.settings import API_NAME
from taxi.api import CarResource
from travels.api import TravelRequestResource
from account.api import ProfileResource, SessionResource

v1_api = Api(api_name=API_NAME)
v1_api.register(CarResource(), canonical=False)
v1_api.register(TravelRequestResource(), canonical=False)
v1_api.register(SessionResource(), canonical=False)
