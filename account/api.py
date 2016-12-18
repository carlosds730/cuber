# our imports
from util.api import BasicResource, BasicAPIException
from account.models import Profile

# tastypie imports
from tastypie import fields
from tastypie.resources import Resource
from tastypie.exceptions import Unauthorized
from tastypie.http import HttpUnauthorized

# django imports
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


class ProfileResource(BasicResource):
    class Meta(BasicResource.Meta):
        queryset = Profile.objects.all()
        resource_name = Profile.RESOURCE_NAME
        fields = ['username', 'first_name', 'last_name', 'last_login', 'photo']
        list_allowed_methods = []
        detail_allowed_methods = ['get']


class SessionObject(object):
    def __init__(self, kwargs=None):
        self.kwargs = kwargs


class SessionResource(Resource):
    username = fields.CharField(attribute="username")
    password = fields.CharField(attribute="password")

    class Meta:
        resource_name = 'sessions'
        object_class = SessionObject
        list_allowed_methods = ['post']
        detail_allowed_methods = []

    def obj_create(self, bundle, **kwargs):
        form = AuthenticationForm(bundle.request, data=bundle.data)
        if form.is_valid():
            login(bundle.request, form.get_user())
            return
        raise BasicAPIException(response=HttpUnauthorized("The email or password you entered is incorrect"))
