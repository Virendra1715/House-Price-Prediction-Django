from django.shortcuts import render
import os
import joblib
import pandas as pd
from .models import HousePrediction

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "ml_model",
    "house_price_model.pkl"
)
COLUMN_PATH = os.path.join(
    BASE_DIR,
    "ml_model",
    "model_columns.pkl"
)

model = joblib.load(MODEL_PATH)
columns=joblib.load(COLUMN_PATH)


def index(request):
    return render(request, 'house_price/index.html')

@login_required(login_url="login")
def predict(request):
    prediction = None

    if request.method == "POST":
        bedrooms = float(request.POST["bedrooms"])
        bathrooms = float(request.POST["bathrooms"])
        sqft_living = float(request.POST["sqft_living"])
        sqft_lot = float(request.POST["sqft_lot"])
        floors = float(request.POST["floors"])
        condition = float(request.POST["condition"])
        grade = float(request.POST["grade"])
        sqft_above = float(request.POST["sqft_above"])
        sqft_basement = float(request.POST["sqft_basement"])
        yr_built = float(request.POST["yr_built"])
        yr_renovated = float(request.POST["yr_renovated"])
        sqft_living15 = float(request.POST["sqft_living15"])
        sqft_lot15 = float(request.POST["sqft_lot15"])
        

        data = pd.DataFrame([[
    bedrooms,
    bathrooms,
    sqft_living,
    sqft_lot,
    floors,
    condition,
    grade,
    sqft_above,
    sqft_basement,
    yr_built,
    yr_renovated,
    sqft_living15,
    sqft_lot15
]], columns=columns)
        print(data)
        prediction = model.predict(data)[0]
        HousePrediction.objects.create(

    bedrooms=bedrooms,

    bathrooms=bathrooms,

    sqft_living=sqft_living,

    sqft_lot=sqft_lot,

    floors=floors,

    condition=condition,

    grade=grade,

    sqft_above=sqft_above,

    sqft_basement=sqft_basement,

    yr_built=yr_built,

    yr_renovated=yr_renovated,

    sqft_living15=sqft_living15,

    sqft_lot15=sqft_lot15,

    predicted_price=prediction,
    
    user=request.user,
)

        print("Prediction =", prediction)
        

    return render(
    request,
    "house_price/predict.html",
    {"prediction": prediction}
)


def history(request):
    return render(request, 'house_price/history.html')


def about(request):
    return render(request, 'house_price/about.html')


def contact(request):
    return render(request, 'house_price/contact.html')
def register(request):
    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")  

        if password != confirm_password:
            messages.error(request,"Password do not match")
            return render(request,"house_price/register.html")

        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username is already exists")
            return render(request,"house_price/register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request,"Email is already exists")
            return render(request,"house_price/register.html") 

        User.objects.create_user(
            username=username,
            email=email,
            password=password
            )
        messages.success(request, "Registration successful.")
        return redirect("login")
    return render(request,"house_price/register.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:

            login(request, user)
            messages.success(request, "Users Login")
            return redirect("predict")

        else:

            messages.error(request, "Invalid Username or Password.")
            messages.info(request, "Don't have an account? Please register first.")
            return render(request, "house_price/login.html")

    return render(request, "house_price/login.html")



def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("home")