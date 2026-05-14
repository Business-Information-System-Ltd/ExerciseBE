from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from .views import DepartmentViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
=======
from .models import *
from .serializers import *
from .views import BranchViewSet
router = DefaultRouter()
router.register(r'branches',BranchViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
>>>>>>> 0097eb37591c684269cc832ea653cc79992b9958
