#FILE: roster/views.py
# Create your views here.
from django.shortcuts import render
from roster.models import Course, Student

def home(request):
    context = {
        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
    }
    return render(request, "base.html", context)
