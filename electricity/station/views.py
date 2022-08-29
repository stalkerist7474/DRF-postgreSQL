from urllib import response
from django.shortcuts import render
from .models import Station, Worker
from .serializer import StationSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict

class StationAPIView(generics.ListAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer




#представление без сериализатора
class WorkerAPIView(APIView):
    def get(self, request):
        man = Worker.objects.all().values()
        return Response ({'get worker': list(man)})


    def post(self, request):
        man_add = Worker.objects.create(
            name = request.data['name'],
            position = request.data['position'],
            place_for_work_id = request.data['place_for_work_id'],
        )
        return Response ({'new worker':model_to_dict(man_add)})

