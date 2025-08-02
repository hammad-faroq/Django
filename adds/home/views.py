from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from django.utils.http import urlencode

# Create your views here.
class newView(View):
    def get(self,request):
        """Har dafa pocha gya.Pehla eik dafaf jab auth tak nai """
        # if not request.user.is_authenticated:
        loginurl = reverse('login')+'?'+urlencode({'next': reverse('ads:all')})
        return redirect(loginurl)#this gonna look for the template at registration/login.html adn use taht template automaticallt
        # return render(request, 'registration/login.html')
        # return redirect('cats:all')
    # def post(self,request):
    #      if request.user.is_authenticated:
    #         return redirect('cats:all')
    #      loginurl = reverse('login')+'?'+urlencode({'next': reverse('cats:all')})
    #      return redirect(loginurl)
             

# Create your views here.
