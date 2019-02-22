from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.models import User,Group

def is_member(user, group_name):
    return user.groups.filter(name=group_name).exists()
def adding_user_to_group(user,group_name):
    my_group = Group.objects.get(name=group_name)
    #print(my_group)
    my_group.user_set.add(user)
# Create your views here.
def remove_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    #print(post.title,post.text,post.author)
    Post.objects.filter(author=post.author,text=post.text,title=post.title).delete()
    #posts = Post.objects.filter( published_date__lte=timezone.now()).order_by('published_date')
    return start_page(request)




def post_edit(request, pk):
    if not request.user.is_authenticated:
        start_page(request)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.published_date = timezone.now()
            if parser_for_video_url(post.video_url):
                post.video_url = parser_for_video_url(post.video_url)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'user_example/post_edit.html', {'form': form})


def buttons(request):
    return render(request,"user_example/buttons2.html")

def video(request):
    a = "asd"


    return render(request, "user_example/video.html")

def parser_for_video_url(url):
    hosts = ["youtube.com","rutube.ru","coub.com","vimeo.com","youtu.be"]
    if "embed" in url:
        return url
    for j in hosts:
        if j in url:
            url = url.replace(j,j+"/embed")
            #print(url)
            return url
    return False


def post_new(request):
    #print(parser_for_video_url("https://rutube.ru/video/cd148e0f2363751812686e84899a5200/?pl_id=5255&pl_type=tag"))

    if not request.user.is_authenticated:
        start_page(request)
    if request.method == "POST":

        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            #
            #print(request.user.username)
            #user = authenticate(username="Artem", password="coding123")#Тут меняй Artem на Nikita
            print(request.user)
            print("lul")
            if not request.user.is_authenticated:
                start_page(request)
            post.author = request.user
            ##
            post.published_date = timezone.now()
            if parser_for_video_url(post.video_url):
                post.video_url = parser_for_video_url(post.video_url)
            post.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'user_example/post_edit.html', {'form': form})

def profle_new(request):
    if not request.user.is_authenticated:
        start_page(request)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            #
            #print(request.user.username)
            #user = authenticate(username="Artem", password="coding123")#Тут меняй Artem на Nikita
            print(request.user)
            print("lul")
            if not request.user.is_authenticated:
                start_page(request)
            post.author = request.user
            ##
            post.published_date = timezone.now()
            post.save()
            return redirect('profile_detail', pk=post.pk)
    else:
        form = ProfileForm()
    return render(request, 'user_example/profile_edit.html', {'form': form})

def profile_detail(request, pk):
    post = get_object_or_404(Profile, pk=pk)
    return render(request, 'user_example/profile_detail.html', {'post': post})

def post_detail(request, pk):
    #print(request.user.username)
    #print(1)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'user_example/post_detail.html', {'post': post})
def index(request):
    return render(request,"user_example/index.html")
def start_page(request):
    posts = Post.objects.filter().order_by('rating')
    posts = posts.reverse()
    ### Нужно сделать срез (с какого рейтингу постить)
    ### Здесь можно сортануть еще по дате , просто сортануть posts по времени
    return render(request,"user_example/start_page.html", {'posts': posts})

def working_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = posts.reverse()
    return render(request,"user_example/working_page.html", {'posts': posts})

def profile(request):
    username1 = request.user.username
    print(username1)
    profiles = Profile.objects.filter(author=request.user)#, title=username1) ### мы нашли наш профайл #### Возможно убрать поиск по title это ник он может быть любым не равным логину, но это плохо для постов

    if len(profiles)== 0:
        ### Нужно создать профайл
        print(1)
        return redirect('profile_new' )
        #pass
    else:
        profiles = profiles[0]
        #print(len(profiles))

        #print(is_member(request.user,"group1"))
        return render(request,"user_example/profile.html", {"postss":profiles})
def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        #print(2)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            #print(username,password)
            user = authenticate(username = username,password = password)
            my_group = Group.objects.get(name='group1')
            print(my_group)
            my_group.user_set.add(user)
            login(request,user)
            return redirect("start_page")
    else:

        form = UserCreationForm()
    context = {"form": form}
    return render(request,"registration/register.html",context)









def my_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        #print(form.errors)
        #print(1)
        if (form.is_valid()):
            #print(2)
            form.save()
            #print(1)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            #print()
            user = authenticate(username=username, password=password)
            if user is not None:

                login(request, user)
                return redirect("index")
                # Redirect to a success page.

            else:
                #print("lul")
                return redirect("index")
    else:
        form = UserCreationForm(request.POST)
    context = {"form": form}
    return render(request,"registration/ls.html",context)

