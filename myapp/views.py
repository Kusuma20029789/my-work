from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def page2_view(request):
    return render(request, 'page2.html') 

def form_view(request):
    return render(request, 'form.html')

def b2_view(request):
    return render(request, 'b2.html')

def b3_view(request):
    return render(request, 'b3.html')
 