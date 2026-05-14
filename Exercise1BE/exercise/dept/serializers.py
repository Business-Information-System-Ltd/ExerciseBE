from rest_framework import serializers
<<<<<<< HEAD
from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__' 
=======
from .models import Branch
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'
>>>>>>> 0097eb37591c684269cc832ea653cc79992b9958
