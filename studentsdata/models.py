from django.db import models

# Board
class Board(models.Model):
    student_board= models.CharField(max_length=20)
    

# Medium model
class Medium(models.Model):
    student_medium= models.CharField(max_length=30)
    


# Standard Model
class Standard(models.Model):
    student_standard=models.IntegerField(default=0)

# Addresses
class Address(models.Model):
    postal_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    

# This is class model
class Students(models.Model):
    student_name = models.CharField(max_length=30)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    medium = models.ForeignKey(Medium, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
