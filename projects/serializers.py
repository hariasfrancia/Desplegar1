from rest_framework import serializers
from .models import Alumno

class AlumnoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'