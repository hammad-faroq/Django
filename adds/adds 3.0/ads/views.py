
from .models import Ad,Comment,Favorite
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from ads.forms import CreateForm, CommentForm



# class AdListView(OwnerListView):
#     model = Ad
#     # By convention:
#     # template_name = "myarts/article_list.html"
class AdListView(OwnerListView):
    model = Ad
    template_name = "ads/ad_list.html"#to show the all the fav when web is reloaded by the user 

    def get(self, request) :
        thing_list = Ad.objects.all()
        # print(thing_list)
        favorites = list()
        if request.user.is_authenticated:
            # rows = [{'id': 2}, {'id': 4} ... ]  (A list of rows)
            rows = request.user.favorite_things.values('id')#this gonna send an aemply list if user dont ahve any favoutires
            # favorites = [2, 4, ...] using list comprehension
            favorites = [ row['id'] for row in rows ]
        ctx = {'thing_list' : thing_list, 'favorites': favorites}
        return render(request, self.template_name, ctx)


class AdDetailView(OwnerDetailView):
    model = Ad
    # model = Forum
    template_name = "ads/ad_detail.html"
    def get(self, request, pk) :
        x = get_object_or_404(Ad, id=pk)
        comments = Comment.objects.filter(Ad=x).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'ad' : x, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)


# class AdCreateView(OwnerCreateView):
#     model = Ad
    # List the fields to copy from the Article model to the Article form
    # fields = ['title', 'text','price',"picture"]
class AdCreateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)

# class AdUpdateView(OwnerUpdateView):
#     model = Ad
    # fields = ['title', 'text','price',"picture"]
    # This would make more sense
    # fields_exclude = ['owner', 'created_at', 'updated_at']
class AdUpdateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')

    def get(self, request, pk):
        pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=pic)#the form gonna have the previus data when called 
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.save()

        return redirect(self.success_url)




class AdDeleteView(OwnerDeleteView):
    model = Ad

def stream_file(request, pk):##THis function gonna have a sepecail url pattern to show the picture ins seprate tab
    pic = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response





class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, Ad=f)
        comment.save()
        return redirect(reverse('ads:ad_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "ads/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        Ad = self.object.Ad
        return reverse('ads:ad_detail', args=[Ad.id])
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')#we dont need a scrf tokken for this post requst bec it is simplea fav/unfav thing
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Add PK",pk)
        t = get_object_or_404(Ad, id=pk)
        fav = Favorite(user=request.user, ad=t)#beacuse the constucotr wants ad not things 
        print(fav)
        try:
            fav.save()  # In case of duplicate key
        except IntegrityError:
            pass
        return HttpResponse("Favorite added 42")

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Delete PK",pk)
        t = get_object_or_404(Ad, id=pk)
        try:
            Favorite.objects.get(user=request.user, ad=t).delete()
        except Favorite.DoesNotExist:
            pass

        return HttpResponse("Favorite deleted 42")

# Create your views here.
