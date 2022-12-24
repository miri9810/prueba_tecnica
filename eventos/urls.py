from django.urls import path
from .views import EventosAPI, BoletosCompraAPIView, BoletosCanjeAPIView, EventosPutAPIView

urlpatterns = [
    path('eventos/reg/', EventosAPI.as_view(),),
    path('eventos/<int:pk>/', EventosPutAPIView.as_view(),),
    path('compra/<int:pk>/', BoletosCompraAPIView.as_view(),),
    path('canje/<int:pk>/', BoletosCanjeAPIView.as_view(),),
]