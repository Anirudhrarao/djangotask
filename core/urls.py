from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('drform/',views.drsign,name='drform'),
    path('ptform/',views.ptsign,name='ptform'),
    path('drlogin/',views.drlogin,name='drlogin'),
    path('ptlogin/',views.ptlogin,name='ptlogin'),
    path('prof/',views.profile,name="profile"),
    path('logout/',views.logout_view,name="logout"),
    path('blog_create/',views.blog_create,name='blog_create'),
    path('blogs/',views.blog_post,name="blogs"),
    path('blogs/<id>/',views.detail_blog,name="blogs_details")
]
