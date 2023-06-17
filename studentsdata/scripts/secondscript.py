from studentsdata.models import Address, Board, Medium, Standard, Students
from studentsdata.services.commands import create_student

def run():
    # Option 3
    # Cretate student from script

    Student=create_student(
        Student_Name="Abhinav Rajpoot",
        Board_id=2, 
        Medium_id=1,
        Standard_id=3,
        City="Dewas",
        Postal_Address="S-7, Santi Nagar"
    )

    Student.save()
    print("Student Created Successfully!!!")




