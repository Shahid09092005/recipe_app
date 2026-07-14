from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User # to register the user
from django.contrib import messages # pass error message
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    people = [
        {'name': 'Alice', 'age': 30 , 'hobbies': ['Reading', 'Traveling', 'Cooking'], 'state': 'California'},
        {'name': 'Bob', 'age': 12 , 'hobbies': ['Gaming', 'Hiking', 'Photography'], 'state': 'New York'},
        {'name': 'Charlie', 'age': 35  , 'hobbies': ['Swimming', 'Cycling', 'Gardening'], 'state': 'Texas'},
        {'name': 'David', 'age': 28 , 'hobbies': ['Running', 'Painting', 'Music'], 'state': 'Florida'},
        {'name': 'Eve', 'age': 32 , 'hobbies': ['Yoga', 'Dancing', 'Writing'], 'state': 'Washington'},
            ]
    page= "Home page"
    return render(request, 'index.html' ,  context={'people': people, 'page':page})

@login_required(login_url='/user_login')
def recipe(request):
    if request.method == 'POST':
        # Handle form submission here
        # You can access form data using request.POST dictionary
    # to take data from frontend and send to backend
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_price=data.get('recipe_price')
        recipe_description=data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        # vegtable.objects.create will create a new instance of the vegetable model and save it to the database. The create() method is a shortcut for creating and saving an object in one step.
        # It takes the field names as keyword arguments and assigns the corresponding values to those fields.
        Vegetable.objects.create(
            user = request.user, # Connect every recipe with a registered user
            recipe_name=recipe_name,
            recipe_price=recipe_price,
            recipe_description=recipe_description,
            recipe_image=recipe_image
        )
    
    data_query=Vegetable.objects.filter(user=request.user) ## shows only recipe that register by that user
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        data_query = Vegetable.objects.filter(user=request.user,recipe_name__icontains=search_query)
    return render(request, 'recipe.html', context={'data_query': data_query , 'page':"Recipe Page"})

def get_delete_recipe(request,recipe_id):
    recipe = Vegetable.objects.get(id=recipe_id,user=request.user)
    # Delete the recipe object from the database
    recipe.delete()
    # Redirect back to the recipe page after deletion
    return redirect('/recipe')

def get_update_recipe(request, recipe_id):
    # Retrieve the recipe object based on the provided recipe_id
    recipe_data = Vegetable.objects.get(id=recipe_id,user=request.user)
    # We use again 'post' method because we want to update the recipe and we want to send the updated data to the backend so we use post method
    if request.method == 'POST':
        # why request.POST because we want to send the updated data to the backend so we use post method
        data = request.POST
        recipe_data.recipe_name = data.get('recipe_name')
        recipe_data.recipe_price = data.get('recipe_price')
        recipe_data.recipe_description = data.get('recipe_description')
        # Check if a new image is uploaded
        if 'recipe_image' in request.FILES:
            recipe_data.recipe_image = request.FILES['recipe_image']
        # Save the updated recipe object to the database
        recipe_data.save()
        # Redirect back to the recipe page after updating
        return redirect('/recipe')
    # If it's a GET request, render the update form with existing recipe data
    page_title = "Update Recipe"
    return render(request, 'recipe.html', context={'recipe_data': recipe_data, 'page': page_title})

def user_register(request):
    if request.method == 'POST':
        # You can access form data using request.POST dictionary
        data=request.POST
        fullname = data.get('fullname')
        gmail = data.get('gmail')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        # make gmail as user name 
        currUserName = gmail
        # check is there user already exist
        existUser = User.objects.filter(username = currUserName).first()
        if existUser: 
            messages.error(request, "Gmail already register")
            return render(request ,'register.html', context={'page':'Register Page'})
        else:
        # if usser not exist so add in the model
            # check password is equal to checkpassword
            if password!=confirm_password:
                messages.error(request,"Password does not match")
                return render(request,'register.html',context={'page':'Register Page'})
            else: # password and confirm_passowrd are equal
                # create_user() save password in hashed format automatically save in User's model
                user = User.objects.create_user(
                first_name=fullname,
                email=gmail,
                username=currUserName,
                password=password
                )
                user.save()
                messages.error(request, "Successful Register")
                return render(request,'login.html',context={'page':"Login Page"})
    # if user not register
    return render(request,'register.html',context={'page':'Register Page'})
              
def user_login(request):
    if request.method =='POST':
        # fetch given details
        data = request.POST
        userName = data.get('gmail')
        userPassword = data.get('password')
        # authnticate check username and password exist if any thing is wrong then it return none
        user = authenticate(request,username=userName,password=userPassword)
        if user is not None:
            login(request, user)
            return redirect('/recipe')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request,'login.html',context={'page':'Register Page'})

def user_logout(request):
    # Log out the user
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('user_login')   # use your login url name


def success_page(request):
    return HttpResponse("<h1>Success! You have reached the success page.</h1>")

def home(request):
    page= "Home page"
    return render(request, 'index.html' , context = {'page' : page} )

def contact(request):
    page= "Contact page"
    return render(request, 'contact.html', context = {'page' : page} )

def about(request):
    page= "About page"
    return render(request, 'about.html', context = {'page' : page} )

# all working correctly now try to live this project