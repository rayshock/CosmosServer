"""
Definition of views.
"""

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse

from django.shortcuts import render, redirect

from django.template import RequestContext
from datetime import datetime
from .models import GameUser
from app.forms import *

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
        

        return render(
            request,
            'game.html',
            {
                'username':request.user.get_username(),
                'coin':0,
            }
        )
    else:
        return redirect( 'login' )

def getCoin(request):
    #pk = request.POST.get('pk', None) # ajax 통신을 통해서 template에서 POST방식으로 전달
    #post = get_object_or_404(Post, pk=pk)
    #post_like, post_like_created = post.like_set.get_or_create(user=request.user)

    
   
    #t = GameUser.objects.get( id=1)
    #t.coin += 1
    #t.save() 
    request.user.coin += 1
    request.user.save()
    return  JsonResponse({'coin':request.user.coin})


def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        # 유효성 검증에 통과한 경우 (username의 중복과 password1, 2의 일치 여부)
        if signup_form.is_valid():
            # SignupForm의 인스턴스 메서드인 signup() 실행, 유저 생성
            signup_form.signup()
            return redirect('game')
    else:
        signup_form = SignupForm()

    context = {
        'signup_form': signup_form,
    }
    return render(request, 'signup.html', context)