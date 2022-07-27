#request and respons ar views.py
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from firstapiproject.models import Contact
from firstapiproject.serializers import ContactSerializer
from rest_framework.response import Response

from rest_framework import status
from rest_framework.decorators import api_view


#weather ar views.py
from pydoc import describe
from django.shortcuts import render
import requests,datetime

#request and response work start ar views.py
@api_view(['GET', 'POST'])
def api_list(request):
    if request.method == 'GET':
        snip = Contact.objects.all()
        serializer = ContactSerializer(snip, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def api_detail(request, pk):
  
    try:
        snip = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactSerializer(snip)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactSerializer(snip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    


#weather ar views.py
def index(request):
    
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='Dhaka'
      
    appid='f827a6fcb7bce5924bf7905be800ed73'
    URL='http://api.openweathermap.org/data/2.5/weather'
    PARAMS={'q':city, 'appid':appid, 'units':'metric'}
    
    r=requests.get(url=URL, params=PARAMS)
    res=r.json()
    description=res['weather'][0]['description']
    icon=res['weather'][0]['icon']
    temp=res['main']['temp']
    day=datetime.date.today
    
    return render(request, 'weatherapp/index.html', {'description':description,
            'icon':icon, 'temp':temp, 'day':day, 'city':city})
    