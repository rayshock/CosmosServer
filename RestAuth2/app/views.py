"""
Definition of views.
"""

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse

from django.shortcuts import render, redirect
from rest_framework import viewsets


from django.template import RequestContext
from datetime import datetime
from .models import *
from app.forms import *

from app.serializer import UserSerializer, CxSerializer

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
import random
#class LoginView(APIView):
#    """ 로그인 """

#    def post(self, request, format=None):
#        serializer = LoginSerializer(data=request.data)
#        if serializer.is_valid(raise_exception=True):
#            ret = serializer.validated_data
#        return Response(ret)

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



@csrf_exempt
@api_view(['POST'])
@authentication_classes(( TokenAuthentication, BasicAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticated,))
def setupCx(request):

    request.user.curCx_id = request.POST['curCxDBID']
    request.user.curUnit_id = request.POST['curUnitDBID']
 
    return  JsonResponse({'data':UserSerializer(request.user).data})



@csrf_exempt
@api_view(['GET'])
@authentication_classes(( TokenAuthentication, BasicAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticated,))
def setupNewPlayer(request):

    
    plantae = Unit()
    plantae.name = "Plantae"
    plantae.kingdom = 1
    plantae.save()
    request.user.units.add( plantae )

    cx = Cx()
    # 나중에 유일한 렌덤값을 생성하도록 고치자.
    cx.name = "B" + "%07d" % random.randint(0,9999999)
    cx.owner = plantae
    cx.save()
    request.user.cxs.add(cx)

    animalia = Unit()
    animalia.name = "Animalia"
    animalia.kingdom = 0
    animalia.save()
    request.user.units.add( animalia )

    return  JsonResponse({'data':UserSerializer(request.user).data})


@csrf_exempt
@api_view(['GET'])
@authentication_classes(( TokenAuthentication, BasicAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticated,))
def user(request):
    return  JsonResponse(UserSerializer(request.user).data)


@csrf_exempt
@api_view(['GET'])
@authentication_classes(( TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def getCoin(request):
    #pk = request.POST.get('pk', None) # ajax 통신을 통해서 template에서 POST방식으로 전달
    #post = get_object_or_404(Post, pk=pk)
    #post_like, post_like_created = post.like_set.get_or_create(user=request.user)

    
   
    #t = GameUser.objects.get( id=1)
    #t.coin += 1
    #t.save() 
    
    curUnit = request.user.units.all()[ request.user.curUnit_id ]
    print( curUnit )
    #curUnit = Unit.objects.get( id=request.user.curUnit_id )
    curUnit.energy += 1
    curUnit.save()
    #curUnit.save()
    request.user.save()
    return  JsonResponse({'coin':curUnit.energy})





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


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    """

    API endpoint that allows users to be viewed or edited.

    """

    queryset = User.objects.all()

    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated,)


class CxViewSet(viewsets.ReadOnlyModelViewSet):

    """

    API endpoint that allows users to be viewed or edited.

    """

    queryset = User.objects.all()

    serializer_class = CxSerializer
    #permission_classes = (IsAuthenticated,)

