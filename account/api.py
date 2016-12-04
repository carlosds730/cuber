from util.api import BasicResource
from account.models import Profile


class ProfileResource(BasicResource):
    class Meta(BasicResource.Meta):
        queryset = Profile.objects.all()
        resource_name = Profile.RESOURCE_NAME
        fields = ['username', 'first_name', 'last_name', 'last_login', 'photo']
        list_allowed_methods = []
        detail_allowed_methods = ['get']
