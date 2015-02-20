from api.models import Country, Place, Target
from rest_framework import serializers


class TargetSerializer(serializers.ModelSerializer):
    # places = serializers.ManyRelatedField(source='places.name', child_relation=Place)
    # places = serializers.HyperlinkedRelatedField(view_name='place-detail', queryset=Place.objects.all(), many=True)


    class Meta:
        model = Target
        fields = ('url', 'first_name', 'last_name', 'other_name', 'phone_no', 'photo', 'places')


class PlaceSerializer(serializers.ModelSerializer):
    # country = serializers.HyperlinkedRelatedField(view_name='country-detail', read_only=True)
    # country = CountrySerializer(queryset=Country.objects.all())

    class Meta:
        model = Place
        fields = ('url', 'id', 'country', 'name')


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    places = PlaceSerializer(many=True)

    class Meta:
        model = Country
        fields = ('url', 'id', 'name', 'places')