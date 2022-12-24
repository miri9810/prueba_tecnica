import datetime
from rest_framework import serializers
from django.forms import DateInput, ValidationError
from .models import Eventos
from django.forms import ValidationError
from rest_framework.response import Response


class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = ('id', 'nombre', 'inicio', 'fin', 'lugar', 'detalle', 'disponibles', 'vendidos', 'canjeados')

        def validate(self, attrs):
            inicio = attrs.get('inicio')
            fin = attrs.get('fin')

            if 'fecha_actual' >= inicio:
                fecha_actual = datetime.date.today()
                raise serializers.ValidationError('No es posible registrar este evento')

            if fin < 'fecha_actual':
                fecha_actual = datetime.date.today()
                print(fecha_actual)
                raise serializers.ValidationError('La fecha de cierre es inválida')

            return attrs


        def create(self, validated_data):
            evento = Eventos.objects.create(**validated_data)
            return evento

class VentaBoletosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = ('id', 'disponibles', 'vendidos')

        def create(self, validated_data):
            vender = Eventos.objects.create(
                vendidos = validated_data.get('vendidos')
            )

            if vender.vendidos != 0:
                boletos_vendidos = vender.disponibles - vender.vendidos
                vender.disponibles = boletos_vendidos
                if vender.disponibles <= 0:
                    raise ValidationError('El número de boletos que deseas comprar no es válido, solo quedan: '+ vender.disponibles)
            
            vender.save()
            return vender


class CanjeoEventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = ('id', 'vendidos', 'canjeados')

        def create(self, validated_data):
            canje = Eventos.objects.create(
                canjeados = validated_data.get('canjeados')
            )

            if canje.canjeados != 0:
                boletos_canjeados = canje.vendidos - canje.canjeados
                canje.vendidos = boletos_canjeados
                if canje.vendidos <= 0:
                    raise ValidationError('El número de boletos que deseas canjear no es válido, solo quedan: '+ canje.vendidos)
                canje.save()
            return canje