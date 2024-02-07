from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['name', 'user']


class Expense(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2)
    quantity = models.IntegerField(null=True)
    date = models.DateField(null=True)


class ExpenseAttribute(models.Model):
    TYPES = [
        ('float', 'Number'),
        ('choices', 'Choices')
    ]
    name = models.CharField(max_length=255)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    attr_type = models.CharField(choices=TYPES)
    unit = models.CharField(max_length=10, null=True)
