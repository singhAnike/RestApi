from django.db import models

class BOARD(models.Model):
    Board= models.CharField(max_length=20)
    

# Medium model
class MEDIUM(models.Model):
    Medium= models.CharField(max_length=30)
    


# Standard Model
class STANDARD(models.Model):
    Standard=models.IntegerField(default=0)
    

# This is class model
class STUDENT(models.Model):
    Student_Name=models.CharField(max_length=30)
    Student_Board=models.ForeignKey(BOARD, on_delete=models.CASCADE)
    Student_Standard=models.ForeignKey(STANDARD, on_delete=models.CASCADE)
    Student_Medium=models.ForeignKey(MEDIUM, on_delete=models.CASCADE)