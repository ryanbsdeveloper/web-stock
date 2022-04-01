from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import EstoqueViewSet

router = SimpleRouter()
router.register('estoque', EstoqueViewSet)



