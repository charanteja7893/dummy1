from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'charan','age':22}
    return render(request,'data_rander.html',context=d)