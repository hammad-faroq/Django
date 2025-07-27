from django.urls import path
from . import views
app_name="polls"
# urlpatterns=[
#     path("",views.index,name="index"),
#     path("<int:question_id>/",views.detail,name="detail"),
#     path("<int:question_id>/results/",views.result,name="results"),
#     path("<int:question_id>/vote/",views.vote,name="vote"),
#     path("<int:question_id>/detail1",views.new_detail, name="new_detail")
# ]

#using generic views
urlpatterns=[
    path("",views.IndexView.as_view(),name="index"),
    path("<int:pk>/",views.DetailView.as_view(),name="detail"),
    path("<int:pk>/results/",views.ResultView.as_view(),name="results"),
    path("<int:question_id>/vote/",views.vote,name="vote"),
    path("<int:question_id>/detail1",views.new_detail, name="new_detail"),
]