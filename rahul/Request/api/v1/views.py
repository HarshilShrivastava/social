from Request.api.v1.serializer import(
    RequestSerializer,
    ConfirmedSerializer,
    ConfirmedReadSerializer,
    RequestSerializer,
    RequestReadSerializer
)
from Request.models import(
    Request,
    Confirmed
)

from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework.authentication import (
    TokenAuthentication
    )
from Profile.models import (
    Profile
)

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def add_friend_request( request, To,From):
    context={}
    data={}
    Profile_to=get_object_or_404(Profile,pk=To)
    Profile_from=get_object_or_404(Profile,pk=From)
    try:
        obj=Request.objects.get(From=Profile_from,To=Profile_to)
    except:
        context['sucess']=True
        obj=Request.objects.create(From=Profile_from,To=Profile_to)
        context['status']=200
        context['message']="request sent"
        context['data']=data
        return Response(context)
    
    context['sucess']=False
    context['status']=400
    context['message']="already  sent"
    context['data']=data
    return Response(context)


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def accept_request( request, id):
    context={}
    data={}
    obj=get_object_or_404(Request,pk=id)
    sender=obj.From
    receiver=obj.To
    print(sender)
    print(receiver)
    try:
        obj=Confirmed.objects.get(Sender=sender,Receiver=receiver)
        obj=Confirmed.objects.get(Sender=receiver,Receiver=sender)
    except:    
        obj1=Confirmed.objects.create(Sender=sender,Receiver=receiver)
        obj2=Confirmed.objects.create(Sender=receiver,Receiver=sender)
        obj.delete()
        context['sucess']=True
        context['status']=200
        context['message']="request accepted"
        context['data']=data
        return Response(context)
    context['sucess']=False
    context['status']=401
    context['message']="error"
    context['data']=data
    return Response(context)


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def reject_request(request,id):
    context={}
    data={}
    try:
        obj=get_object_or_404(Request,pk=id)
    except:
        context['sucess']=False
        context['status']=401
        context['message']="already rejeced or not found"
        context['data']=data
        return Response(context)
    obj.delete()
    context['sucess']=True
    context['status']=200
    context['message']="request rejected sucessfully"
    context['data']=data
    return Response(context)

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def remove_friend(request,id):
    context={}
    data={}
    try:
        obj=get_object_or_404(Confirmed,pk=id)
    except:
        context['sucess']=False
        context['status']=401
        context['message']="already removed or not found"
        context['data']=data
        return Response(context)
    sender=obj.Receiver
    receiver=obj.Sender
    obj1=Confirmed.objects.get(Sender=sender,Receiver=receiver)
    obj1.delete()
    obj.delete()
    context['sucess']=True
    context['status']=200
    context['message']="sucessfully unfriend"
    context['data']=data
    return Response(context)


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def list_of_recived_request(request):
    profileobj=get_object_or_404(Profile,User=request.user)
    qs=Request.objects.filter(To=profileobj)
    serializer=RequestReadSerializer(qs,many=True)
    context={}
    data={}
    context['sucess']=True
    context['status']=200
    context['message']="sucessfully got list"
    data=serializer.data
    context['count']=qs.count()
    context['data']=data
    return Response(context)


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def list_of_sent_request(request):
    profileobj=get_object_or_404(Profile,User=request.user)
    qs=Request.objects.filter(From=profileobj)
    serializer=RequestReadSerializer(qs,many=True)
    context={}
    data={}
    context['sucess']=True
    context['status']=200
    context['message']="sucessfully got list"
    data=serializer.data
    context['count']=qs.count()
    context['data']=data
    return Response(context)

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def list_of_friends(request):
    profileobj=get_object_or_404(Profile,User=request.user)
    qs=Confirmed.objects.filter(Sender=profileobj)
    serializer=ConfirmedReadSerializer(qs,many=True)
    context={}
    data={}
    context['sucess']=True
    context['status']=200
    context['message']="sucessfully got list"
    data=serializer.data
    context['count']=qs.count()
    context['data']=data
    return Response(context)

