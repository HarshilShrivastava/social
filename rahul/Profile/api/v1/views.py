from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import UpdateAPIView
from Profile.models import(
    Profile,
    Status
)
from django.contrib.auth import (
    authenticate,
    get_user_model,
)

from Profile.api.v1.serializer import (
    ProfileSerializer,
    ProfileReadSerializer,
    StatusSerializer,
    StatusReadSerializer

)

User = get_user_model()

class CustumerProfile(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def post(self, request, *args, **kwargs):
        context={}
        data={}
        if request.user.IS_CUSTOMER==1:
            serializer=ProfileSerializer(data=request.data)
            if serializer.is_valid():
                obj=serializer.save(User=self.request.user)
                obj.save()
                context['status']=200
                context['sucess']=True
                context['message']="sucessfully created"
                data=serializer.data
                context['data']=data
                return Response(context)
            else:
                context['status']=400
                context['sucess']=False
                context['message']="not  created"
                data=serializer.errors
                context['data']=data
                return Response(context)
        else:
            context['status']=400
            context['sucess']=False
            context['message']="Unauthorised acess "
            data=serializer.errors
            context['data']=data
            return Response(context)
    def get(self, request, *args, **kwargs):
        context={}
        data={}
        if request.user.IS_CUSTOMER == 0:
            context['sucess']=False
            context['status']=400
            context['message']="Unauthorised acess"
            context['data']=data
            return Response(context)

        try:
            profile=get_object_or_404(Profile  ,User=request.user)
            print(profile)
        except:
            context['sucess']=False
            context['status']=400
            context['message']="fill the form"
            context['data']=data
            return Response(context)
        serializer=ProfileReadSerializer(profile)
        context['sucess']=True
        context['status']=200
        context['message']="already exist"
        data=serializer.data
        context['data']=data
        return Response(context)
    
    def put(self,request,*args, **kwargs):
        context={}
        data={}
        if request.user.IS_CUSTOMER== 1:
            obj=get_object_or_404(Profile,User=request.user)
            serializer = ProfileSerializer(obj,data=request.data)
            if serializer.is_valid():
                serializer.save(User=self.request.user)
                context['status']=200
                context['sucess']=True
                context['message']="sucessfully created"
                data=serializer.data
                context['data']=data
                return Response(context)
            context['sucess']=False
            context['status']=400
            context['message']="fill the form"
            context['data']=data
            return Response(context)
        else:
            context['sucess']=False
            context['status']=400
            context['message']="Unauthorised acess"
            context['data']=data
            return Response(context)

class StatusView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    
    def post(self, request, *args, **kwargs):
        context={}
        data={}
        if request.user.IS_CUSTOMER==1:
            serializer=StatusSerializer(data=request.data)
            profileobj=get_object_or_404(Profile,User=request.user)
            if serializer.is_valid():
                if serializer.is_valid():
                    obj=serializer.save(profile=profileobj)
                    obj.save()
                    context['status']=200
                    context['sucess']=True
                    context['message']="sucessfully created"
                    
                    data=serializer.data
                    context['data']=data
                    return Response(context)
                else:
                    context['status']=400
                    context['sucess']=False
                    context['message']="not  created"
                    data=serializer.errors
                    context['data']=data
                    return Response(context)
            else:
                context['status']=400
                context['sucess']=False
                context['message']="Unauthorised acess "
                data=serializer.errors
                context['data']=data
                return Response(context)
    def get(self, request, *args, **kwargs):
        context={}
        data={}
        if request.user.IS_CUSTOMER == 0:
            context['sucess']=False
            context['status']=400
            context['message']="Unauthorised acess"
            context['data']=data
            return Response(context)

        try:
            profileobj=get_object_or_404(Profile  ,User=request.user)
        except:
            context['sucess']=False
            context['status']=400
            context['message']=""
            context['data']=data
            return Response(context)
        qs=Status.objects.filter(profile=profileobj, Timestamp=timezone.timedelta(days=1)
)

        serializer=StatusReadSerializer(qs,many=True)
        context['sucess']=True
        context['status']=200
        context['message']="already exist"
        context['count']=qs.count()
        data=serializer.data
        context['data']=data
        return Response(context)

class StatusViewDetail(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def put(self, request, pk,*args, **kwargs):
        context={}
        data={}
        if request.user.IS_CUSTOMER == 0:
            context['sucess']=False
            context['status']=400
            context['message']="Unauthorised acess"
            context['data']=data
            return Response(context)
        try:
            Statusobj=get_object_or_404(Status,pk=pk)
        except:
            context['sucess']=False
            context['status']=400
            context['message']="does not exist"
            context['data']=data
            return Response(context)
        serializer=StatusSerializer(Statusobj,data=request.data)
        if serializer.is_valid():
            obj=serializer.save(Profile=profileobj)
            obj.save()
            context['status']=200
            context['sucess']=True
            context['message']="sucessfully updated"
            data=serializer.data
            context['data']=data
            return Response(context)
        else:
            context['sucess']=False
            context['status']=400
            context['message']="can't update"
            context['data']=data
            return Response(context)
    def delete(self, request, pk,*args, **kwargs):
        context={}
        data={}
        if request.user.IS_CUSTOMER == 0:
            context['sucess']=False
            context['status']=400
            context['message']="Unauthorised acess"
            context['data']=data
            return Response(context)
        try:
            Statusobj=get_object_or_404(Status,pk=pk)
        except:
            context['sucess']=False
            context['status']=400
            context['message']="does not exist"
            context['data']=data
            return Response(context)
        Statusobj.delete()
        context['status']=200
        context['sucess']=True
        context['message']="sucessfully updated"
        data=serializer.data
        context['data']=data
        return Response(context)








