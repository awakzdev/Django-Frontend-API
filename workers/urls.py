from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('workers', views.WorkerView)
router.register('jobs', views.JobView)
router.register('paradigms', views.ParadigmView)

urlpatterns = [
    path('', include(router.urls))
]