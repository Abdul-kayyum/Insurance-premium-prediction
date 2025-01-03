from django.shortcuts import render
# import joblib
import pickle
# # Create your views here.
# model = joblib.load("static/insurance_model_rf.h5")
model =  pickle.load(open('static/insurance-model-rf.pk1' , 'rb'))

def homepage(request):
    return render(request, "homepage.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def results(request):
    return render(request, "results.html")

def prediction(request):
    if request.method == "POST":
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        bmi = int(request.POST.get('bmi'))
        smoker = int(request.POST.get('smoker'))
        children = int(request.POST.get('children'))
        region = int(request.POST.get('region'))

        predict = round(model.predict([[age,sex,bmi,children,smoker,region]])[0])

        if (sex and smoker) == 1:
            sex, smoker = "Male", "Yes"
        else:
            sex, smoker = "Female", "No"

        if region == 0:
            region = "Southwest"
        elif region == 1:
            region = "Southeast"
        elif region == 2:
            region = "Northwest"
        else:
            region = "Northeast"

        output = {
            "age":age,
            "sex":sex,
            "bmi":bmi,
            "smoker":smoker,
            "children":children,
            "region":region,
            "output":predict
        }
        return render(request,"results.html",output)
    else:
        return render(request, "prediction.html")