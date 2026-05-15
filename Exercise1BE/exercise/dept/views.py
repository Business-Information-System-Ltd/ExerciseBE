from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer