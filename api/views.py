from django.shortcuts import render
from . models import Student
from . serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Model objects - Single Student data
def student_detail(request,pk):
    #st = Student.objects.get(id=2)
    st = Student.objects.get(id=pk)
    serializer = StudentSerializer(st)
    print(st)
    print(serializer)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')

# Query set All Student data
def student_list(request):
    #st = Student.objects.get(id=2)
    st = Student.objects.all()
    serializer = StudentSerializer(st, many=True)
    print(st)
    print(serializer)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')
