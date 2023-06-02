from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from studentsdata.models import Students
from django.http import Http404
from studentsdata.serializers import StudentSerializer

class StudentsList(APIView):
    """
    List all students details, or create a new students data.
    """
    def get(self, request):
        all_students = Students.objects.all()
        serializer = StudentSerializer(all_students, many=True)
        return Response(serializer.data)

    def post(self, request):
       
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# fecthing individuals data

class student_detail(APIView):

    def stu_object(self, pk):
        try:
            return Students.objects.get(pk=pk)
        except Students.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.stu_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
