from api.models import Country, Place, Target
from rest_framework import serializers


class PlaceSerializer(serializers.ModelSerializer):
    # def __init__(self, *args, **kwargs):
    #     many = kwargs.pop('many', True)
    #     super(PlaceSerializer, self).__init__(many=many, *args, **kwargs)
    # country = serializers.HyperlinkedRelatedField(view_name='country-detail', read_only=True)
    # country = CountrySerializer(queryset=Country.objects.all())

    class Meta:
        model = Place
        fields = ('url', 'id', 'country', 'name')


class TargetSerializer(serializers.ModelSerializer):
    # places = serializers.ManyRelatedField(source='places.name', child_relation=Place)
    # places = serializers.HyperlinkedRelatedField(view_name='place-detail', queryset=Place.objects.all(), many=True)
    # places = PlaceSerializer(many=True)

    class Meta:
        model = Target
        fields = ('url', 'first_name', 'last_name', 'other_name', 'phone_no', 'photo', 'places')


class TargetSerializerList(serializers.ModelSerializer):

    places = PlaceSerializer(many=True)

    class Meta:
        model = Target
        fields = ('url', 'first_name', 'last_name', 'other_name', 'phone_no', 'photo', 'places')


class CountrySerializerList(serializers.HyperlinkedModelSerializer):
    # places = PlaceSerializer(many=True)

    class Meta:
        model = Country
        fields = ('url', 'id', 'name')


class CountrySerializerDetail(serializers.HyperlinkedModelSerializer):
    places = PlaceSerializer(many=True)

    class Meta:
        model = Country
        fields = ('url', 'id', 'name', 'places')