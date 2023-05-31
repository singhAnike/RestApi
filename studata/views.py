from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from studata.models import STUDENT
from django.http import Http404
from studata.serializers import StudentSerializer

class StudentsList(APIView):
    """
    List all students details, or create a new students data.
    """
    def get(self, request):
        students = STUDENT.objects.all()
        serializer = StudentSerializer(students, many=True)
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
            return STUDENT.objects.get(pk=pk)
        except STUDENT.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.stu_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)


















# from django.shortcuts import render, HttpResponse, redirect
# from django.http import HttpResponse, JsonResponse
# from django.views import View
# from studata.models import STANDARD, STUDENT, BOARD, MEDIUM
# from django.views.decorators.csrf import csrf_exempt
# from studata.serializers import STUDENTSerializer
# from rest_framework.parsers import JSONParser

# Create your views here.
# class Welcome(View):
#     def get(self, request):
#         return HttpResponse("!!!!!Hello Welcome to this Student Management system!!!!!")

# def create_student(request):
#     if request.method == 'POST':
#         student_name = request.POST['student_name']
#         board_name = request.POST['board_name']
#         standard = request.POST['standard']
#         medium = request.POST['medium']
        
#         board = BOARD.objects.get(Board=board_name)
#         stan=STANDARD.objects.get(Standard=standard)
#         medi=MEDIUM.objects.get(Medium=medium)
#         student = STUDENT(Student_Name=student_name, Student_Board=board, Student_Standard=stan, Student_Medium=medi)
#         student.save()        
#         return redirect("datatable/")
    
#     # Passing Optional data which is availabe in form
#     B= BOARD.objects.all()
#     M= MEDIUM.objects.all()
#     S= STANDARD.objects.all()
#     context={
#         'B':B,
#         'M':M,
#         'S':S
#     }
#     return render(request, 'create_student.html', context)

# def student_table(request):
#     students=STUDENT.objects.all()
#     return render(request, 'table.html', {'students':students})


# @csrf_exempt
# def Studentjson_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         students = STUDENT.objects.all()
#         serializer = STUDENTSerializer(students, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = STUDENTSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

