from tastypie.resources import ModelResource
from tastypie.authentication import MultiAuthentication, ApiKeyAuthentication, \
    SessionAuthentication


class BasicResource(ModelResource):
    class Meta:
        authentication = MultiAuthentication(ApiKeyAuthentication(), SessionAuthentication())
        list_allowed_methods = []
        detail_allowed_methods = ['get']
