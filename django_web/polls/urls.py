from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'wxy', views.index1, name='index1'),
]

'''
to call the view, we need to map it to a url
'''