from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy
from .models import Make,Auto
from .forms import MakeForm,MakeAuto
#Do do tomorrow
#1 First i will have to understand the datacase scheme and the realtion between the two models or tables defined
#2 Then I will maybe have to watch the vidoes again to get naunence of the db visually running
#3 Understand the login and Loginmixier behind the scenes
#4 Undetstanding the forms, MakeForm(Biuldin django), generic Drug operations, next keyword amd reversse_lazy
#5then i will complete this assignment of course (: all of thses stuff is not medium level and is not foloow the instructins now, I will build all the things from
#scratch and will figure out how it is working uder the hood, and then i will do it the Djago vay, i mean in few lines after getting
#the understtanding of the working under the covers so see you tomorrow (:

# Create your views here.
class MainView(LoginRequiredMixin,View):
    """this is the main page"""
    def get(self, request):
        mc = Make.objects.count()
        al = Auto.objects.all()

        ctx = {'make_count': mc, 'auto_list': al}
        return render(request, 'autos/auto_list.html', ctx)
class MakeView(LoginRequiredMixin,View):
    """Viewing all the makes"""
    def get(self,request):
        make=Make.objects.all()
        context={"make_list":make}
        return render(request,"autos/make_list.html",context)
    

class MakeCreate(LoginRequiredMixin,View):
    """Add a make of the page"""
    template="autos/make_form.html"
    success_url=reverse_lazy("autos:all")
    def get(self,request):
        form=MakeForm()
        contex={"form":form}
        return render(request,self.template,contex)
    def post(self,request):
        form=MakeForm(request.POST)
        if not form.is_valid():
            context={"form":form}
            return render(request,self.template,context)
        form.save()
        return redirect(self.success_url)
class MakeUpdate(LoginRequiredMixin, View):
    """Update the auto if exist"""
    model=Make
    success_url=reverse_lazy("autos:all")
    template="autos/make_form.html"
    def get(self,request,pk):
        make=get_object_or_404(self.model,pk=pk)
        form = MakeForm(instance=make)
        ctx = {'form': form}
        return render(request, self.template, ctx)
    def post(self,request,pk):
        make=get_object_or_404(self.model,pk=pk)#get the previouls obj again becuase post forgte it 
        form=MakeForm(request.POST,instance=make)#update the previous one with this new one
        if not form.is_valid():
            context={"form":form}
            return render(request,self.template,context)#we are sending a 200 if form is not valid in post, solution we can just redirect it to the get again but some other day 
        form.save()
        return redirect(self.success_url)
class MakeDelete(LoginRequiredMixin,View):
    model=Make
    template="autos/make_confirm_delete.html"
    success_url = reverse_lazy("autos:all")
    def get(self,request,pk):
        make=get_object_or_404(self.model,pk=pk)
        con={"make":make}
        return render(request, self.template,con)
    def post(self,request,pk):
        make=get_object_or_404(self.model,pk=pk)
        make.delete()
        return redirect(self.success_url)
class AutoCreate(LoginRequiredMixin, View):
    template="autos/auto_form.html"
    success_url=reverse_lazy("autos:all")
    def get(self,request):
        form=MakeAuto()
        context={"form":form}
        return render(request,self.template,context)
    def post(self,request):
        form=MakeAuto(request.POST)
        if not form.is_valid():
            context={"form":form}
            return render (request, self.template,context)
        form.save()
        return redirect(self.success_url)
class AutoUpdate(LoginRequiredMixin, View):
    model=Auto
    template="autos/auto_form.html"
    success_url = reverse_lazy("autos:all")
    def get(self,request,pk):
        auto=get_object_or_404(self.model,pk=pk)
        form=MakeAuto(instance=auto)
        context={"form":form}
        return render(request,self.template,context)
    def post(self,request,pk):
        auto=get_object_or_404(self.model,pk=pk)
        form=MakeAuto(request.POST,instance=auto)
        if not form.is_valid():
            context={"form":form}
            return render(request,self.template,context)
        form.save()
        return redirect(self.success_url)
class AutoDelete(LoginRequiredMixin,View):
    model=Auto
    template="autos/auto_confirm_delete.html"
    success_url = reverse_lazy("autos:all")
    def get(self,request,pk):
        auto=get_object_or_404(self.model,pk=pk)
        con={"auto":auto}
        return render(request,self.template,con)
    def post(self,request,pk):
        auto=get_object_or_404(self.model,pk=pk)
        auto.delete()
        return redirect(self.success_url)




        


