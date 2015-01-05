#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from opinion.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_opinion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', main_page),
    url(r'^write/', write_page),
    url(r'^writeComment', write_comment),
    url(r'^register/', register_page),
    url(r'^login/', login_page),
    url(r'^logout/', logout),
    url(r'^link/(?P<query>\d+)', write_page_query_no),
    url(r'^view/no/(?P<query>\d+)', view_page_query_no),
    url(r'^view/tag/(?P<query>\d+)', view_page_query_tag),
    url(r'^view', view_page),
    #url(r'^userinfo', userinfo_page),
    url(r'^admin/', include(admin.site.urls)),
)
