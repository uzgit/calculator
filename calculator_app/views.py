from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CalculateForm

class Calculator:

    def __init__(self):

        return

    def handle_calculation(self, calculation):

        result = None

        try:
            result = eval(calculation)
            
        except(ZeroDivisionError):
            result = "You can't divide by 0!!!"

        return result

calculator = Calculator()

# Create your views here.
def calculate(request):
    calculation = None
    result = None


    if request.method == "GET":
        print("in GET")

    elif request.method == "POST":
        form = CalculateForm(request.POST)
        if form.is_valid():
            calculation = form.cleaned_data["calculation"]
            result = calculator.handle_calculation(calculation)

            print("calculation: {}".format(calculation))
            print("result: {}".format( result ))

    form = CalculateForm()
    return render(request, "calculate.html", {"form" : form, "calculation" : calculation, "result" : result})

