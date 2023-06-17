from studentsdata.models import Address, Students, Board, Medium, Standard

def create_student(
        Student_Name: str, Board_id:int, Medium_id:int, 
        Standard_id:int, City: str, Postal_Address: str
    )-> Students:

    student_address = Address.objects.create(
        postal_address=Postal_Address,
        city=City
    )

    studentboard = Board.objects.get(id=Board_id)
    studentmedium = Medium.objects.get(id=Medium_id)
    studentstandard = Standard.objects.get(id=Standard_id)

    student = Students.objects.create(
        student_name=Student_Name,
        board=studentboard,
        medium=studentmedium,
        standard=studentstandard,
        address=student_address
    )
    return student
