from django.utils import timezone
from drf_haystack.viewsets import HaystackViewSet
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

# from rest_framework_extensions.mixins import (
#     CacheResponseAndETAGMixin,
# )
# from rest_framework_extensions.cache.mixins import (
#     CacheResponseMixin,
# )
from . import (
    models,
    serializers,
)


class RoomCategoryViewSet(ReadOnlyModelViewSet):
    queryset = models.RoomCategory.objects.all()
    serializer_class = serializers.RoomCategorySerializer
    permission_classes = (
        AllowAny,
    )


class RoomViewSet(ReadOnlyModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    permission_classes = (
        AllowAny,
    )
    filter_fields = (
        'category',
    )


class FloorViewSet(ReadOnlyModelViewSet):
    queryset = models.Floor.objects.all()
    serializer_class = serializers.FloorSerializer
    permission_classes = (
        AllowAny,
    )


class BuildingViewSet(ReadOnlyModelViewSet):
    queryset = models.Building.objects.all()
    serializer_class = serializers.BuildingSerializer
    permission_classes = (
        AllowAny,
    )


class OrganizationViewSet(ReadOnlyModelViewSet):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    permission_classes = (
        AllowAny,
    )


class PersonViewSet(ReadOnlyModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    permission_classes = (
        AllowAny,
    )


class EventViewSet(ReadOnlyModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    permission_classes = (
        AllowAny,
    )

    def get_queryset(self):
        return self.queryset.filter(show_end__gte=timezone.now())