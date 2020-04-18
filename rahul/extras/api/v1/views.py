from Profile.models import(
    Profile
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
from extras.api.v1.serializer import (
    ProfileSerializer
)

from Profile.api.v1.serializer import (
    ProfileReadSerializer

)

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def confirm_Profile(request):
    context={}
    data={}
    if request.method == 'POST':
        serializer=ProfileSerializer(request.POST)
        no=serializer.data['Phone_Number']
        print(no)
        try:
            obj=get_object_or_404(Profile,Phone_Number=no)
        except:
            context['sucess']=False
            context['status']=404
            context['message ']="Not registered"
            context['data']=data
            return Response(context)
        context['sucess']=True
        context['status']=200
        context['message ']=" registered"
        profile=ProfileReadSerializer(obj)
        data=profile.data
        context['data']=data
        return Response(context)
        
