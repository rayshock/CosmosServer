"""
Definition of urls for RestAuth2.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from app import views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
# admin.autodiscover()

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)



from rest_framework.authtoken import views


urlpatterns = [


    # Examples:
    #url(r'^$', app.views.home, name='home'),
    #url(r'^contact$', app.views.contact, name='contact'),
    #url(r'^about', app.views.about, name='about'),
    #url(r'^login/$',
    #    django.contrib.auth.views.login,
    #    {
    #        'template_name': 'app/login.html',
    #        'authentication_form': app.forms.bootstrapauthenticationform,
    #        'extra_context':
    #        {
    #            'title': 'log in',
    #            'year': datetime.now().year,
    #        }
    #    },
    #    name='login'),
    #url(r'^logout$',
    #    django.contrib.auth.views.logout,
    #    {
    #        'next_page': '/',
    #    },
    #    name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^accounts/', include('django.contrib.auth.urls')),

    #url(r'^accounts/profile/', app.views.game, name='game'),

    #url(r'^$', app.views.game, name='game'),
    url(r'^admin/', admin.site.urls, name='admin'),
   
    url(r'^game/', app.views.game, name='game'),
    
    url(r'^getCoin/', app.views.getCoin, name='getCoin'),

    url(r'^user/', app.views.user, name='user'),

    url(r'^setupNewPlayer/', app.views.setupNewPlayer, name='setupNewPlayer'),
    
    url(r'^setupCx/', app.views.setupCx, name='setupCx'),

    #url(r'^signup/', app.views.signup, name='signup'),
    url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),

]
