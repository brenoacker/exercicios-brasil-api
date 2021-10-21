from django.db.models import fields
from rest_framework import serializers
from exercicios.models import DDD, Regiao, SiglaEstado


class DDDSerializer(serializers.ModelSerializer):
    class Meta:
        model = DDD
        fields = ['ddd',]
        
class RegiaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regiao
        fields = ['A', 'B', 'C']

class SiglaEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiglaEstado
        fields = ['sigla',]