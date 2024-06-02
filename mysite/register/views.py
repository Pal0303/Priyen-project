from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render, redirect

def login(request):
    if 'id_user' in request.session or 'id_company' in request.session:
        return redirect('index')  # Assuming 'index' is your home page URL name
    return render(request, 'login.html')

def logincandidate(request):
    if 'id_user' in request.session or 'id_company' in request.session:
        return redirect('index')  # Assuming 'index' is your home page URL name
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Perform authentication logic here, redirect if successful, otherwise handle errors
    return render(request, 'login.html')

def employer_login(request):
    if 'id_user' in request.session or 'id_company' in request.session:
        return redirect('index')  # Assuming 'index' is your home page URL name
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Perform authentication logic here, redirect if successful, otherwise handle errors
    return render(request, 'employer_login.html')