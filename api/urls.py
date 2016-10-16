from tastypie.api import Api

from taxi.api import CarResource

v1_api = Api(api_name="v1")
v1_api.register(CarResource())
