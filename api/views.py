from api.models import Country, Place, Target
from rest_framework import filters
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from api.serializers import CountrySerializerList, CountrySerializerDetail, PlaceSerializer, TargetSerializer, TargetSerializerList

# Create your views here.


class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'other_name', 'places__name')

    # override to use a slightly modified serializer
    # framework doesn't support nested serializers for create

    def list(self, request):
        queryset = Target.objects.all()
        queryset = self.filter_queryset(queryset)
        serializer = TargetSerializerList(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Target.objects.all()
        target = get_object_or_404(queryset, pk=pk)
        serializer = TargetSerializerList(target, context={'request': request})
        return Response(serializer.data)


class CountryViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Country.objects.all()
        serializer = CountrySerializerList(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Country.objects.all()
        country = get_object_or_404(queryset, pk=pk)
        serializer = CountrySerializerDetail(country, context={'request': request})
        return Response(serializer.data)


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer