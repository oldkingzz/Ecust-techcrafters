# navi/views.py
import json
from .models import course_model
from django.shortcuts import render, get_object_or_404
def index(request):
    courses = course_model.objects.all()
    courses_data = [{'course_name': course.course_name, 'ppt': course.ppt.url, 'long_text': course.long_text, 'notes': course.notes.url} for course in courses]
    return render(request, 'navi/index.html', {'courses': courses, 'course_data': json.dumps(courses_data)})

def navi_view(request, course_name):
    course = get_object_or_404(course_model, course_name=course_name)
    all_courses = course_model.objects.all()
    courses_data = [{'course_name': course.course_name, 'ppt': course.ppt, 'long_text': course.long_text, 'notes': course.notes} for course in all_courses]
    div2_data = [{'course_name': course.course_name} for course in all_courses]
    return render(request, 'navi/index.html', {'course': course, 'all_courses': all_courses,'div2_data': div2_data})
