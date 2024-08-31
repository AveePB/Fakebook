from django.http.request import HttpRequest
from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden, HttpResponse
from django.shortcuts import render
from django.views import View

from authz.credentials_service import *

# Create your views here.
class LoginView(View):
    # Handles GET requests
    def get(self, request: HttpRequest):
        return render(request, 'login.html')
    
    # Handles POST requests
    def post(self, request: HttpRequest):
        # Inspect json body
        username = request.POST.get('username')
        password = request.POST.get('password')

        if (not username or not password): 
            return HttpResponseBadRequest("Invalid form data")
        
        # Inspect user data
        if (checkCredentials(username, password)):
            # Return JWT
            return HttpResponse(status=200)
        else:
            return HttpResponseNotFound("User credentials are invalid")


class SignupView(View):
    # Handles GET requests
    def get(self, request: HttpRequest):
        return render(request, 'signup.html')

    # Handles POST requests
    def post(self, request: HttpRequest):
        # Inspect json body
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (not username or not password): 
            return HttpResponseForbidden("Invalid form data")
        
        # Inspect user data
        try:
            validateUsername(username)
            validatePassword(password)
        except FieldRequired:
            return HttpResponseForbidden("Invalid form data")
        except CriteriaError:
            return HttpResponseBadRequest("Username must be alphanumeric and has 5-32 characters,\npassword must have 6-32 characters")
        except UsernameTakenError:
            return HttpResponseForbidden("Username is already taken")
        
        print("IS taken:", UserCredentials.objects.filter(username=username). exists())

        # Save new user credentials
        new_usercredentials = UserCredentials(username=username)
        new_usercredentials.set_password(password)
        new_usercredentials.save(force_insert=True)
        return HttpResponse(status=204)