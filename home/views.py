from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializers import PeopleSerializer, RegisterSerializer, LoginSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.paginator import Paginator

class RegisterAPI(APIView):
    
    def post(self, request):
        data = request.data
        serializer=RegisterSerializer(data=data)
        
        if not serializer.is_valid():
            return Response({
                'status':False,
                'messasge': serializer.errors,
            },status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({
            'status':True,
            'messasge': 'User Register Successzfully.',
        },status.HTTP_201_CREATED)

class LoginAPI(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status':False,
                'messasge': serializer.errors,
            },status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=serializer.data['username'],password=serializer.data['password'])
        
        if not user:
            return Response({
                'status':False,
                'messasge': "Username or password Invalid.",
            },status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'status':True,
            'messasge': 'User Logged in Successfully.',
            'token':str(token)
        },status.HTTP_200_OK)

@api_view(['GET','POST','PUT'])
def index(request):
    if request.method == 'GET':
        courses={
            "name":"Python",
            "price":2000,
            "Duration":"3 month",
            "module":[1,2,3,4,5],
            "search":request.GET.get('search')
        }
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        return Response({"message":"This is post method","data":data})
    else:
        return Response({"message":"Method is not valid!"})
    
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def people(request):
    if request.method == "GET":
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "PUT":
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "PATCH":
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "DELETE":
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({"message":"Person Deleted."})

class PersonAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            objs = Person.objects.all()
            page = request.GET.get('page',1)
            page_size = 3
            paginator=Paginator(objs,page_size)
            serializer = PeopleSerializer(paginator.page(page),many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({
                'status':False,
                'message':"Page not found.",
                'error':str(e)
            })
    def post(self,request):
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self,request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def patch(self,request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({"message":"Person Deleted."})
    