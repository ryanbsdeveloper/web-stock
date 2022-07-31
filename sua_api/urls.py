from django.urls import path
from . import views

urlpatterns = [
    path('API/', views.APIView.as_view(), name='api')
]


