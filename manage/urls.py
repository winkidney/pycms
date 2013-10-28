#coding:utf-8
#urls of manage
from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pycms.views.home', name='home'),
    # url(r'^pycms/', include('pycms.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^$',views.home),
    url(r'^makepost/$',views.make_post),
    url(r'^edit/(\d{1,10})/$',views.modify_post),
    
)