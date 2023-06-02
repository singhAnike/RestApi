from django.contrib import admin
from studentsdata.models import Board, Medium, Standard, Students, Address

# Register your models here.
admin.site.register(Students)
admin.site.register(Board)
admin.site.register(Standard)
admin.site.register(Medium)
admin.site.register(Address)

