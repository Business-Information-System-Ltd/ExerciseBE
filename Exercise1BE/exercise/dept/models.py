from django.db import models

class Department(models.Model):
    dept_code = models.CharField(max_length=50, unique=True)
    dept_name = models.CharField(max_length=255)
    status = models.BooleanField(default=True) # Active ဆိုရင် True, Inactive ဆိုရင် False

    def __str__(self):
        return self.dept_name