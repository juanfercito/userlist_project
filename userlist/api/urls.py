from rest_framework.routers import DefaultRouter

# pylint: disable=import-error
from userlist.api.views import UsuarioViewSet

router = DefaultRouter()
router.register('usuarios', UsuarioViewSet, basename='usuario')
urlpatterns = router.urls
