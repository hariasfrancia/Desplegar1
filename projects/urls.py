from rest_framework import routers
from .api import AlumnoViewSets

router = routers.DefaultRouter()
router.register('api/Alumno',AlumnoViewSets,'projects')


urlpatterns = router.urls