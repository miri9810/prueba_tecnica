from rest_framework.test import APITestCase
from .serializers import EventosSerializer, VentaBoletosSerializer, CanjeoEventosSerializer
from .models import Eventos

# Create your test here

eventos_data = {
    "nombre":"DevFest",
    "inicio":"2019-12-02",
    "fin":"2019-12-03",
    "lugar":"CMDX Virtual",
    "detalle":"Evento realizado por Google"
}

class TestSerializerEventos(APITestCase):
    def setUp(self):

        self.data = eventos_data
        self.data["nombre"] = eventos_data["nombre"]
        self.data["inicio"] = eventos_data["inicio"]
        self.data["fin"] = eventos_data["fin"]
        self.data["lugar"] = eventos_data["lugar"]
        self.data["detalle"] = eventos_data["detalle"]

    def test_create_eventos(self):
        serializer = EventosSerializer(data=self.data)

        self.assertTrue(serializer.is_valid(), serializer.errors)
        self.result_dic = serializer.save()

        self.assertNotEqual(self.result_dic, None)
        self.assertTrue(isinstance(self.result_dic, Eventos))
