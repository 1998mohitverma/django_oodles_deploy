from django.shortcuts import render, HttpResponseRedirect
from .models import Student_table
from .forms import Student_form
from django.views import View
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.

# method:1 by using function based view:

def add_and_show_student(request):
    if request.method == 'POST':
        fm = Student_form(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            contact = fm.cleaned_data['contact']
            course = fm.cleaned_data['course']
            city = fm.cleaned_data['city']
            pwd = fm.cleaned_data['password']
            reg = Student_table(name=name, email=email, contact=contact, course=course, city=city, password=pwd)
            reg.save()
            fm = Student_form()
    else:
        fm = Student_form()
    stud = Student_table.objects.all()
    return render(request, 'crud/student.html',{'form':fm,'stu':stud})

def update_student(request, id):
    if request.method == 'POST':
        pi = Student_table.objects.get(pk=id)
        fm = Student_form(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi = Student_table.objects.get(pk=id)
        fm = Student_form(instance=pi)    
    return render(request, 'crud/update.html',{'form':fm})    


def delete_data(request, id):
    if request.method == 'POST':
        pi = Student_table.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# method:2 by using class base view:------------------------------------

# class Add_student(View):
#     def get(self, request):
#         fm = Student_form()
#         stud = Student_table.objects.all()
#         return render(request, 'crud/student.html',{'form':fm,'stu':stud})
#     def post(self,request):
#         fm = Student_form(request.POST)
#         if fm.is_valid():
#             fm.save()
#             fm = Student_form()
#             return HttpResponseRedirect('/')


# class Delete_view(View):
#     def post(self, request, id):
#         pi = Student_table.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/')

# class Update_view(View):
#     def get(self,request, id):
#         pi = Student_table.objects.get(pk=id)
#         fm = Student_form(instance=pi)
#         return render(request, 'crud/update.html', {'form':fm})
#     def post(self, request, id):
#         pi = Student_table.objects.get(pk=id)
#         fm = Student_form(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#             return HttpResponseRedirect('/')

#: method:3 class based view using TemplateView and RedirectView----------------

# class UserAddShowView(TemplateView):
#     template_name = 'crud/student.html'
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         fm = Student_form()
#         stud = Student_table.objects.all()
#         context = {'stu':stud, 'form':fm}
#         return context
        
#     def post(self, request):
#         fm = Student_form(request.POST)
#         if fm.is_valid():
#             fm.save()
#             return HttpResponseRedirect('/')

# # This Class will Update/Edit
# class UserUpdateView(View):
#   def get(self, request, id):
#     pi = Student_table.objects.get(pk=id)
#     fm = Student_form(instance=pi)
#     return render(request, 'crud/update.html', {'form':fm})
  
#   def post(self, request, id):
#     pi = Student_table.objects.get(pk=id)
#     fm = Student_form(request.POST, instance=pi)
#     if fm.is_valid():
#       fm.save()
#       return HttpResponseRedirect('/')

# # This Class will Delete
# class UserDeleteView(RedirectView):
#   url = '/'
#   def get_redirect_url(self, *args, **kwargs):
#     del_id = kwargs['id']
#     Student_table.objects.get(pk=del_id).delete()
#     return super().get_redirect_url(*args, **kwargs)