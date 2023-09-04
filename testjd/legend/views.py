from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Person_a, Person_b

def index(request):
    people_a = Person_a.objects.all()
    people_b = Person_b.objects.all()
    return render(request, 'legend/index.html', {'people_a': people_a, 'people_b': people_b})

def legend_detail_A(request, person_name):
    # 使用get_object_or_404并指定正确的模型名字
    person_a = get_object_or_404(Person_a, name=person_name)


    return render(request, 'legend/legend_detail.html', {'person_a': person_a})

def legend_detail_B(request, person_name):
    # 使用get_object_or_404并指定正确的模型名字
    person_b = get_object_or_404(Person_b, name=person_name)


    return render(request, 'legend/legend_detail_mec.html', {'person_b': person_b})
