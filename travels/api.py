from util.api import BasicResource
from tastypie import fields
from travels.models import TravelRequest
from account.api import ProfileResource


class TravelRequestResource(BasicResource):
    # client = fields.ForeignKey(ProfileResource, 'client')

    class Meta(BasicResource.Meta):
        queryset = TravelRequest.objects.all()
        resource_name = TravelRequest.RESOURCE_NAME
        fields = ['when', 'duration', 'assigned_car', 'assigned_driver']
        list_allowed_methods = ['post', 'get']
        detail_allowed_methods = ['get', 'put']