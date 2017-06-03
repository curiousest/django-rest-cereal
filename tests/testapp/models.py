
from django.db import models


class A(models.Model):
    title = models.CharField(max_length=100)
    b = models.ForeignKey('B', null=True, on_delete=models.CASCADE)


class B(models.Model):
    title = models.CharField(max_length=100)
    c = models.ForeignKey('C', null=True, on_delete=models.CASCADE)


class C(models.Model):
    title = models.CharField(max_length=100)
    a = models.ForeignKey(A, null=True, on_delete=models.CASCADE)



