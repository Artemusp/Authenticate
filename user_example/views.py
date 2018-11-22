from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.models import User


# Create your views here.
def buttons(request):
    return render(request,"user_example/buttons2.html")

def post_new(request):

    if request.method == "POST":

        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)

            print(request.user.username)
            user = authenticate(username="Artem", password="coding123")#Тут меняй Artem на Nikita

            post.author = user

            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'user_example/post_edit.html', {'form': form})
def post_detail(request, pk):
    print(request.user.username)
    print(1)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'user_example/post_detail.html', {'post': post})
def index(request):
    return render(request,"user_example/index.html")
def start_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,"user_example/start_page.html", {'posts': posts})
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

