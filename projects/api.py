from  rest_framework import viewsets, permissions
from .models import Alumno
from .serializers import AlumnoSerializers

class AlumnoViewSets(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlumnoSerializers
    