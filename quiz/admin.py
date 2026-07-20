from django.contrib import admin
from .models import Course
from .models import Question
from .models import Result
# Register your models here..
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Result)