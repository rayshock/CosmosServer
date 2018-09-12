"""
Definition of views.
"""

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse

from django.shortcuts import render, redirect

from django.template import RequestContext
from datetime import datetime
from .models import GameUser

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def game(request):
    """renders the about page."""
    assert isinstance(request, HttpRequest)



    if request.user.is_authenticated:

        t = GameUser.objects.get( id=1)
        t.coin += 1
        t.save()

        return render(
            request,
            'game.html',
            {
                'username':request.user.get_username(),
                'coin':GameUser.objects.get( id=1).coin,
            }
        )
    else:
        return redirect( 'login' )

def getCoin(request):
    #pk = request.POST.get('pk', None) # ajax 통신을 통해서 template에서 POST방식으로 전달
    #post = get_object_or_404(Post, pk=pk)
    #post_like, post_like_created = post.like_set.get_or_create(user=request.user)

    t = GameUser.objects.get( id=1)
    t.coin += 1
    t.save() 
    return  JsonResponse({'coin':GameUser.objects.get( id=1).coin})