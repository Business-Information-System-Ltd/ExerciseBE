from django.db import models

<<<<<<< HEAD
class Department(models.Model):
    dept_code = models.CharField(max_length=50, unique=True)
    dept_name = models.CharField(max_length=255)
    status = models.BooleanField(default=True) 

    def __str__(self):
        return self.dept_name
=======
class Branch(models.Model):
    
   
    branch_code = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    
  
    Status = models.BooleanField(default=False)

    class Meta:
        db_table = 'branch'

    def __str__(self):
        
        return self.branch_name
    
  
   
>>>>>>> 0097eb37591c684269cc832ea653cc79992b9958
