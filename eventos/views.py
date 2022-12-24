from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Eventos
from .serializers import EventosSerializer, VentaBoletosSerializer, CanjeoEventosSerializer

# Create your views here.

class EventosAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = EventosSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get(self, request):
        queryset = Eventos.objects.filter(status_delete=False) 
        serializer = EventosSerializer(queryset, many=True)
        return Response(serializer.data)



class EventosPutAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        queryset = Eventos.objects.filter(pk=pk, status_delete=False) 
        serializer = EventosSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = get_object_or_404(Eventos, pk=pk, status_delete=False)
        serializer = EventosSerializer(
            instance=queryset,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)



class BoletosCompraAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        queryset = Eventos.objects.filter(pk=pk, status_delete=False) 
        serializer = EventosSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = get_object_or_404(Eventos, pk=pk, status_delete=False)
        serializer = VentaBoletosSerializer(
            instance=queryset,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class BoletosCanjeAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        queryset = Eventos.objects.filter(pk=pk, status_delete=False) 
        serializer = EventosSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = get_object_or_404(Eventos, pk=pk, status_delete=False)
        serializer = CanjeoEventosSerializer(
            instance=queryset,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)