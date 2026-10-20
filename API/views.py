from interviews.models import interview
from rest_framework.viewsets import ModelViewSet
from .serializerAPI import modelserializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .paginations import pagination_pagenumber
from rest_framework.filters import OrderingFilter


class api_response(ModelViewSet):
    queryset=interview.objects.all()
    serializer_class=modelserializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    pagination_class=pagination_pagenumber
    filter_backends=[OrderingFilter]
    ordering_fields=['created_at','update_at','id']
    ordering=['-id']


def createtoken(request):
    token=""
    message=""

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            token,created=Token.objects.get_or_create(user=user)
            token=token.key
            message = "Login successful. Token created."
        else:
            message = "Invalid Details"
        return render(request,'API/key.html',{'message':message,'token_key':token})
    return render(request,'API/login.html')
