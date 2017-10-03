import json
from django.shortcuts import render
from .forms import UpdateData

# Create your views here.

#Access server using http://127.0.0.1:8000/catalog/

def writeData(data):
    fow = open("catalog/data/data.json", "w")
    fow.write(data)
    fow.close()

def readData():
    fo = open("catalog/data/data.json", "r")
    info = fo.read()
    fo.close()
    return info

def index(request):
    #Pass through get by appending url with ?test=data

    if request.method == 'GET':
        data = request.GET['test']
    writeData(data)
    info = readData()
    return render(
        request,
        'index.html',
        context={'info':info}
    )
