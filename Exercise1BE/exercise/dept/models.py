from django.db import models

class Branch(models.Model):
    
   
    branch_code = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    
  
    Status = models.BooleanField(default=False)

    class Meta:
        db_table = 'branch'

    def __str__(self):
        
        return self.branch_name
    
  
   
