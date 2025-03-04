from django.shortcuts import render
from django.http import HttpResponse
from .models import Textbook

def home(request):
    return render(request, 'home.html')

def textbook_list(request):
    textbooks = Textbook.objects.all()
    # Get unique course codes from the Textbook model.
    course_codes = Textbook.objects.values_list('course_code', flat=True).distinct()
    context = {
        'textbooks': textbooks,
        'available_courses': course_codes,
    }
    return render(request, 'textbooks.html', context)

def textbooks_by_course_code(request, course_code):
    textbooks = Textbook.objects.filter(course_code=course_code, availability=True) 
    context = {'textbooks': textbooks, 'course_code': course_code}
    return render(request, 'textbooks_by_coursecode.html', context)