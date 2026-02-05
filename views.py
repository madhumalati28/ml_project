import joblib
import numpy as np
import os
from django.shortcuts import render
from .models import Prediction

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "ml_model", "advertising_model.pkl")
model = joblib.load(model_path)

def index(request):
    return render(request, "index.html")

def home(request):
    prediction = None

    if request.method == "POST":
        tv = float(request.POST['tv'])
        radio = float(request.POST['radio'])
        newspaper = float(request.POST['newspaper'])

        data = np.array([[tv, radio, newspaper]])
        prediction = model.predict(data)[0]

        # save into DB
        Prediction.objects.create(
            tv=tv,
            radio=radio,
            newspaper=newspaper,
            sales_prediction=prediction
        )

    return render(request, "home.html", {"prediction": prediction})
