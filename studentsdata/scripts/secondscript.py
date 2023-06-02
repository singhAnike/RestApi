from studentsdata.models import Address, Board, Medium, Standard, Students
from studentsdata.utils import create_student

"""
from rest_framework import serializers
from serializers import StudentSerializer
"""
def run():
    # Option 3
    # Cretate student from script

    Student=create_student(
        Student_Name="Vishal",
        Board_id=1, 
        Medium_id=2,
        Standard_id=3,
        City="Indore",
        Postal_Address="B-4 Hemu Colony"
    )

    Student.save()
    print("Student Created Successfully!!!")



