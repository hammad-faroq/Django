from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from django.utils.http import urlencode

# Create your views here.
class newView(View):
    def get(self,request):
        if not request.user.is_authenticated:
            loginurl = reverse('login')+'?'+urlencode({'next': reverse('autos:all')})
            return redirect(loginurl)
        # return render(request, 'registration/login.html')
        return redirect('autos:all')
