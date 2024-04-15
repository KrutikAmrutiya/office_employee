from django.db import models

# Create your models here.


# class Department(models.Model):
#     name = models.CharField(max_length=30,null=False)
#     location = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name
#
#
# class Role(models.Model):
#     name = models.CharField(max_length=30, null=False)
#
#     def __str__(self):
#         return self.name


class Employee(models.Model):
    f_name = models.CharField(max_length=30, null=False)
    l_name = models.CharField(max_length=30, null=False)
    #dept = models.IntegerField(max_length=30,null=False)
    dept = models.CharField(max_length=30, null=False)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    #role = models.ForeignKey(Role, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, null=False)
    phone = models.IntegerField(default=0)
    location = models.CharField(max_length=30, default='')
    hire_date = models.DateField()



    def __str__(self):
        return "%s %s %s" %(self.f_name, self.l_name, self.phone)