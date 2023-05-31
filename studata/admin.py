from django.contrib import admin
from studata.models import BOARD, STANDARD, STUDENT, MEDIUM

# Register your models here.
admin.site.register(STUDENT)
admin.site.register(BOARD)
admin.site.register(STANDARD)
admin.site.register(MEDIUM)
