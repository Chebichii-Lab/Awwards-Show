from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url('register/',views.signup, name='registration'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url('logout/',auth_views.LogoutView.as_view(), name='logout'),
    url('profile/', views.profile, name='profile'),
    url(r'^upload/$',views.project,name='add_project'),
    url(r'^project_details/(?P<id>\d+)', views.project_view, name='projectdetails'),
]