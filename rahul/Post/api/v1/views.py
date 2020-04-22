from Post.models import (
    Post,
    Like,
    Comment,
    CommentLike
)
from rest_framework.response import Response
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
    Profile
)
from django.contrib.auth import (
    get_user_model,
)

from Post.api.v1.serializer import (
    PostSerializer,
    PostReadSerializer,
    CommentReadSerializer,
    CommentSerializer,

)
User = get_user_model()
##api for posts
class PostView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def post(self, request, *args, **kwargs):
        context={}
        data={}
        if request.user.IS_CUSTOMER==1:
            serializer=PostSerializer(data=request.data)
            if serializer.is_valid():
                User=get_object_or_404(Profile,User=request.user)
                obj=serializer.save(Profile=User,Archived=False)
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
        if request.user.IS_CUSTOMER==1:
            User=get_object_or_404(Profile,User=request.user)
            qs=Post.objects.filter(Profile=User,Archived=False)
            serializer=PostReadSerializer(qs,many=True)
            context['sucess']=True
            context['status']=200
            context['count']=qs.count()
            context['message']="sucessfully get"
            data=serializer.data
            context['data']=data
            return Response(context)
##api for posts
class PostViewDetail(APIView):

    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def put(self,request,pk,*args, **kwargs):
        context={}
        User=get_object_or_404(Profile,User=request.user)
        data={}
        obj=get_object_or_404(Post,pk=pk)
        if (request.user.IS_CUSTOMER==1)and (obj.Profile.User==request.user):
            obj=get_object_or_404(Post,pk=pk)
            serializer=PostSerializer(obj,data=request.data)
            if serializer.is_valid():
                serializer.save(Profile=User,Archived=False)
                context['sucess']=True
                context['status']=200
                context['message']="sucessfully updated"
                data=serializer.data
                context['data']=data
                return Response(context)
            else:

                context['sucess']=False
                context['status']=400
                context['message']="can't updated"
                data=serializer.errors
                context['data']=data
                return Response(context)
        else:
            context['sucess']=False
            context['status']=401
            context['message']="Unauthorised Acess"
            context['data']=data
            return Response(context)
                        
    def get(self,request,pk,*args, **kwargs):
            context={}
            
            data={}
            obj=get_object_or_404(Post,pk=pk)
            if (request.user.IS_CUSTOMER==1):
                obj=get_object_or_404(Post,pk=pk)
                serializer=PostSerializer(obj)
                context['sucess']=True
                context['status']=200
                context['message']="sucessfully updated"
                data=serializer.data
                context['data']=data
                return Response(context)
                
            else:
                context['sucess']=False
                context['status']=401
                context['message']="Unauthorised Acess"
                context['data']=data
                return Response(context)

    def delete(self,request,pk,*args, **kwargs):
            context={}
            data={}
            
            if (request.user.IS_CUSTOMER==1)and (obj.Profile.User==request.user):
                try:
                    obj=get_object_or_404(Post,pk=pk)
                except:
                    
                    context['sucess']=False
                    context['status']=400
                    context['message']="can't delete"
                    context['data']=data
                    return Response(context)
                obj.Archived=True
                obj.save()
                context['sucess']=True
                context['status']=200
                context['message']="sucessfully deleted"
                context['data']=data
                return Response(context)                
            else:
                context['sucess']=False
                context['status']=401
                context['message']="Unauthorised Acess"
                context['data']=data
                return Response(context)

#api for post to like and unlike
@api_view(['POST',])
@permission_classes((IsAuthenticated, ))
def like(request,pk):
    context={}
    data={}
    obj=get_object_or_404(Post,pk=pk)
    qs=Like.objects.filter(Post=obj)
    Profil=get_object_or_404(Profile,User=request.user)
    try:
        obj1=Like.objects.get(Profile=Profil,Post=obj)
    except:  
        obj1=Like.objects.create(Profile=Profil,Post=obj)
        context['sucess']=True
        context['status']=200
        context['count']=qs.count()
        context['message']="sucessfully Unliked"
        context['data']=data
        return Response(context)
    obj1.delete()
    context['sucess']=True
    context['count']=qs.count()
    context['status']=200
    context['message']="sucessfully liked"
    context['data']=data
    return Response(context)

#api for post to like and unlike
@api_view(['POST',])
@permission_classes((IsAuthenticated, ))
def Commentlike(request,pk):
    context={}
    data={}
    obj=get_object_or_404(Comment,pk=pk)
    qs=CommentLike.objects.filter(Comment=obj)
    Profil=get_object_or_404(Profile,User=request.user)
    try:
        obj1=CommentLike.objects.get(Profile=Profil,Comment=obj)
    except:
        obj1=Like.objects.create(Profile=Profil,Comment=obj)
        context['sucess']=True
        context['status']=200
        context['count']=qs.count()
        context['message']="sucessfully Unliked"
        context['data']=data
        return Response(context)
    obj1.delete()
    context['sucess']=True
    context['count']=qs.count()
    context['status']=200
    context['message']="sucessfully liked"
    context['data']=data
    return Response(context)



class CommentView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def post(self,request, pk, *args, **kwargs):
        context={}
        data={}
        if request.user.IS_CUSTOMER==1:
            serializer=CommentSerializer(data=request.data)
            if serializer.is_valid():
                User=get_object_or_404(Profile,User=request.user)
                Postu=get_object_or_404(Post,pk=pk)
                obj=serializer.save(Profile=User,Post=Postu,Archived=False)
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
            context['data']=data
            return Response(context)
    

    def get(self, request, pk,*args, **kwargs):
        context={}
        data={}
        if request.user.IS_CUSTOMER==1:
            Poste=get_object_or_404(Post,pk=pk)
            qs=Comment.objects.filter(Post=Poste,Parent=None,Archived=False)
            serializer=CommentReadSerializer(qs,many=True)
            context['sucess']=True
            context['status']=200
            context['count']=qs.count()
            context['message']="sucessfully get"
            data=serializer.data
            context['data']=data
            return Response(context)

class CommentViewDetail(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def put(self,request, id,pk, *args, **kwargs):
        context={}
        data={}
        if request.user.IS_CUSTOMER==1:
            Commentobj=get_object_or_404(Comment,pk=id)
            serializer=CommentSerializer(Commentobj,data=request.data)
            if serializer.is_valid():
                User=get_object_or_404(Profile,User=request.user)
                Postobj=get_object_or_404(Post,pk=pk)
                obj=serializer.save(Profile=User,Post=Postobj,Archived=False)
                obj.save()
                context['status']=200
                context['sucess']=True
                context['message']="sucessfully updateed"
                data=serializer.data
                context['data']=data
                return Response(context)
            else:
                context['status']=400
                context['sucess']=False
                context['message']="can't update  "
                data=serializer.errors
                context['data']=data
                return Response(context)
        else:
            context['status']=401
            context['sucess']=False
            context['message']="Unauthorised acess "
            context['data']=data
            return Response(context)



    def delete(self,request, id,pk, *args, **kwargs):
        pk=None
        context={}
        data={}
        if request.user.IS_CUSTOMER==1:
            
            try:
                Commentobj=get_object_or_404(Comment,pk=id)
                Commentobj.Comment='[ Comment Deleted ]'
                Commentobj.save()

            except:
                context['status']=400
                context['sucess']=False

                context['message']="can't delete  "
                context['data']=data
                return Response(context)

            context['status']=200
            context['sucess']=True
            context['message']="sucessfully deleted"
            context['data']=data
            return Response(context)
            




