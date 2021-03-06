from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('speciality', views.SpecialityView)
router.register('workers', views.WorkerView)

urlpatterns = [
    path('', include(router.urls))
]