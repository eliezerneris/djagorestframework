from rest_framework.routers import DefaultRouter
from cadastros.views import Ufs, Cidades, Usuarios

router = DefaultRouter()
router.register(r'ufs', Ufs)
router.register(r'cidades', Cidades)
router.register(r'usuarios', Usuarios)
urlpatterns = router.urls