from django.shortcuts import render
import requests
import pprint
import json

# Create your views here.

def home(request):
    return render(request, 'home.html')

def top(request):
    code = request.GET['code']
    grant_type = 'authorization_code'
    client_id = '{rest-api-key}'
    redirect_uri = 'http://localhost:8000/top'
    # Get access_token!
    param = {
        'grant_type': grant_type,
        'client_id': client_id,
        'redirect_uri' : redirect_uri,
        'code' : code,
    }

    url = 'https://kauth.kakao.com/oauth/token'
    r = requests.post(url, data=param)
    json_result = r.json()
    print(r.json())
    access_token = json_result['access_token']
    return render(request, 'top.html', {'access_token':access_token})


