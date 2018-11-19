from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    return render(request,"user_example/index.html")
def start_page(request):
    return render(request,"user_example/start_page.html")
def profile(request):
    return render(request,"user_example/profile.html")
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(2)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            print(username,password)
            user = authenticate(username = username,password = password)
            login(request,user)
            return redirect("index")
    else:

        form = UserCreationForm()
    context = {"form": form}
    return render(request,"registration/register.html",context)









def my_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form.errors)
        print(1)
        if (form.is_valid()):
            print(2)
            form.save()
            print(1)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            print()
            user = authenticate(username=username, password=password)
            if user is not None:

                login(request, user)
                return redirect("index")
                    # Redirect to a success page.

            else:
                print("lul")
                return redirect("index")
    else:
        form = UserCreationForm(request.POST)
    context = {"form": form}
    return render(request,"registration/ls.html",context)

