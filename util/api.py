from tastypie.resources import ModelResource
from tastypie.authentication import MultiAuthentication, ApiKeyAuthentication, \
    SessionAuthentication
from tastypie.authorization import Authorization
from tastypie.exceptions import TastypieError, Unauthorized
from tastypie.http import HttpResponse, HttpApplicationError


class BasicAPIException(TastypieError):
    def __init__(self, response=None, *args, **kwargs):
        # If there is not response, we assume is a 500 error
        if not response:
            self.response = HttpApplicationError()
        if not isinstance(response, HttpResponse):
            raise ValueError("{0} is not a valid HttpResponse".format(response))
        self.response = response


class UserObjectsOnlyAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list.filter(client__user=bundle.request.user)

    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        if hasattr(bundle.obj, 'client'):
            if bundle.obj.client.user == bundle.request.user:
                return True
            raise Unauthorized
        return True

    def create_detail(self, object_list, bundle):
        if hasattr(bundle.obj, 'client'):
            if bundle.obj.client.user == bundle.request.user:
                return True
        raise Unauthorized

    def update_list(self, object_list, bundle):
        allowed = []
        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if hasattr(obj, 'client'):
                if obj.client.user == bundle.request.user:
                    allowed.append(obj)
        return allowed

    def update_detail(self, object_list, bundle):
        if hasattr(bundle.obj, 'client'):
            if bundle.obj.client.user == bundle.request.user:
                return True
            raise Unauthorized('You are not allowed to update this object')
        return True

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")


class BasicResource(ModelResource):
    class Meta:
        authentication = MultiAuthentication(ApiKeyAuthentication(), SessionAuthentication())
        authorization = UserObjectsOnlyAuthorization()
        list_allowed_methods = []
        detail_allowed_methods = ['get']


class BasicResourceNoAuth(ModelResource):
    class Meta:
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
