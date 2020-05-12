from django.conf.urls import url
from authenticationapp import views

#TEMPLATE URLS!
app_name = 'authenticationapp'


urlpatterns=[
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$',views.user_login, name='user_login'),
]