from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *

<<<<<<< HEAD
from rest_framework import viewsets
from .models import Department
from .serializers import DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer# Create your views here.
=======
class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
>>>>>>> 0097eb37591c684269cc832ea653cc79992b9958
