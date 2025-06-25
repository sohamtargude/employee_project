from django.db import models

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.FloatField()

    class Meta:
        db_table = 'employes'  # matches your MySQL table name exactly

    def __str__(self):
        return f"{self.name} - {self.position}"
