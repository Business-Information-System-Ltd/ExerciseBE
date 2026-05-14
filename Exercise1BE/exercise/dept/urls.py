from django.urls import path, include
from rest_framework.routers import DefaultRouter
from  .views import  BranchViewSet
from .views import DepartmentViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'branches', BranchViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]