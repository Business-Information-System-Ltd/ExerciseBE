from rest_framework import serializers

from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department

        fields = '__all__' 

from .models import Branch
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

      
