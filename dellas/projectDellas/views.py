from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth import authenticate

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            return render(request, 'sucesso', {'usuario': user})
        else:
            return render(request, 'erro')
    else:
        return render(request, 'erro')
