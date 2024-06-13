from rest_framework.views import APIView
from rest_framework.response import Response
# from myapp.serializers import userSerializer
# from myapp.models import New_user
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
###################################
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework import serializers
from myapp.serializers import UserRegister,userSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your views here.
User=get_user_model()
class Register(APIView):

    def post(self,request,format=None):
        
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            data['phone']=account.phone
            
            data['image']=account.image.url
            #print('###########################*************##############',account.image)
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors

        return Response(data)
    
class LoginView(APIView):

    authentication_classes = [TokenAuthentication]

    def post(self, request):
        # Your authentication logic here
        user = authenticate(username=request.data['username'], password=request.data['password'])
        serializer_class=UserRegister(user)
        print('$$$$$$$$$',user.password)
        
        if user:
            token, created = Token.objects.get_or_create(user=user)
            print('jjjjjjjjjjj',token)
            #login user data  and its corresponding token is shown in response
            context={'data':serializer_class.data,'token':token.key,'userid':user.id}
           
            return Response({'status': True,'message': 'login success','context':context})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)

    
class Userview(APIView):
    permission_classes = [IsAuthenticated]
    ## to view only id data
    def get(self,request):
        pt=User.objects.get(id=request.user.id) 
        print('mmmmmmmmmmmmmmmm',pt)
        serializer_class=userSerializer(pt)
        return Response({'status': True,"message":"company data","list":serializer_class.data})
    
    def patch(self,request):
        pt=User.objects.get(id=request.user.id) 
        serializer_class=userSerializer(pt, data=request.data,partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'partial data is updated',"list":serializer_class.data})
        return Response( serializer_class.errors)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response(status=200, data={"message": "Successfully logged out."})
        except (AttributeError, Token.DoesNotExist):
            return Response(status=400, data={"detail": "Token not found."})

