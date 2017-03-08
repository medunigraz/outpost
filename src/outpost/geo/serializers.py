from drf_haystack.serializers import HaystackSerializer
from rest_framework.serializers import (
    IntegerField,
    ModelSerializer,
    SerializerMethodField,
)
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from . import (
    models,
    search_indexes,
)


class RoomSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Room
        geo_field = 'layout'
        exclude = (
            'polymorphic_ctype',
        )
        id_field = 'id'


class RoomSearchSerializer(HaystackSerializer):
    class Meta:
        index_classes = [search_indexes.RoomIndex]
        fields = [
            'text',
        ]


class FloorSerializer(ModelSerializer):
    class Meta:
        model = models.Floor
        exclude = (
            'order',
        )


class BuildingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Building
        geo_field = 'outline'


class DoorSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Door
        geo_field = 'line'
        exclude = (
            'polymorphic_ctype',
        )
        id_field = 'id'


class NodeSerializer(GeoFeatureModelSerializer):

    ctype = SerializerMethodField()

    class Meta:
        model = models.Node
        geo_field = 'center'
        exclude = (
            'polymorphic_ctype',
        )

    def get_ctype(self, obj):
        return obj.polymorphic_ctype.name


class EdgeSerializer(GeoFeatureModelSerializer):
    source_node = NodeSerializer(source='source', many=False)
    destination_node = NodeSerializer(source='destination', many=False)

    class Meta:
        model = models.Edge
        geo_field = 'path'


class RoutingEdgeSerializer(EdgeSerializer):
    sequence = IntegerField(read_only=True)


class BeaconSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Beacon
        geo_field = 'position'
