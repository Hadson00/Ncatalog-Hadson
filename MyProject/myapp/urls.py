from django.urls import path
from myapp.views import *

urlpatterns = [
    path("", index, name="index"),
    path("home/", home, name="home"),
    path('like/<int:clothes_id>/', like_clothes, name='like_clothes'),
    path("comment/<int:clothes_id>/", comment_clothes, name="comment_clothes"),
    path("create/", create, name="create_clothes"),
    path("edit/<int:clothes_id>", edit, name="edit_clothes"),
    path("delete/<int:clothes_id>", delete_clothes, name="delete_clothes"),
]