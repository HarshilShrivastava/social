from rest_framework import status
from rest_framework.response import Response
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

from django.contrib.auth import (
    authenticate,
    get_user_model,
)

from User.api.v1.serializer import (
    RegistrationSerializer,
    UserLoginSerializers,
)

User = get_user_model()

def validate_email(email):
    user = None
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    if user != None:
        return email

@api_view(['POST', ])
@permission_classes([AllowAny,])
@authentication_classes([])
def registration_view(request):
    if request.method == 'POST':
        data = {}
        context={}

        email = request.data.get('email', '0')
        if validate_email(email) != None:
            context['sucess'] = False
            context['response'] = status.HTTP_403_FORBIDDEN
            context['error_message'] = 'That email is already in use.'
            context['data']=data
            return Response(context)

        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            context['sucess'] = True
            context['message'] = 'Sucessfully registered'
            context['response'] = status.HTTP_201_CREATED
            data['email'] = user.email
            data['username'] = user.username
            data['IS_CUSTOMER'] = user.IS_CUSTOMER
        else:
            context['sucess'] = False
            context['message'] = str(serializer.errors['username'][0])
            context['response'] = status.HTTP_401_UNAUTHORIZED
            data = serializer.errors
            context['errror']=data
        context['data']=data


    return Response(context)

@api_view(['POST', ])
@permission_classes((AllowAny,))
def login_view(request):
    if request.method == 'POST':
        serializer = UserLoginSerializers(data=request.data)
        data={}
        context={}
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            account=authenticate(username=username ,password=password)
            if account:
                try:
                    token = Token.objects.get(user=account)
                except Token.DoesNotExist:
                    token = Token.objects.create(user=account)
                context['status']=200
                context['sucess']=True
                context['message']="Sucessfully Created"
                
                data['token'] = token.key
                data['IS_CUSTOMER']=account.IS_CUSTOMER
          
                context['data']=data
                return Response(context)
            else:
                context['status']= 400
                context['sucess'] = False
                context['message'] = 'Invalid credentials'
                context['data']=data
                return Response(context)
        else:
            
            return Response(context)
