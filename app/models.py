from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['name', 'user']


class Expense(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    date = models.DateField(null=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE)


class CustomField(models.Model):
    TYPES = [
        ('float', 'Number'),
        ('choices', 'Text')
    ]
    name = models.CharField(max_length=255)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    field_type = models.CharField(choices=TYPES)
    unit = models.CharField(max_length=10, null=True)


class CustomChoice(models.Model):
    name = models.CharField(max_length=255)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    custom_field = models.ForeignKey(CustomField, on_delete=models.CASCADE)


class CustomFieldValue(models.Model):
    int_value = models.FloatField(null=True)
    text_value = models.ForeignKey(CustomChoice, on_delete=models.CASCADE, null=True)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    custom_field = models.ForeignKey(CustomField, on_delete=models.CASCADE)

