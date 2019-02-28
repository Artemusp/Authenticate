from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import ProfileForm, TaskForm
from .models import Profile, Task
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
    if request.user != post.author:
        return start_page(request)
    #print(post.title,post.text,post.author)
    Post.objects.filter(author=post.author,text=post.text,title=post.title).delete()
    #posts = Post.objects.filter( published_date__lte=timezone.now()).order_by('published_date')
    return start_page(request)




def post_edit(request, pk):
    if not request.user.is_authenticated:
        return start_page(request)
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author:

        return start_page(request)
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
    return render(request,"user_example/modal_boost.html")

def video(request):

    return render(request, "user_example/video.html")

def parser_for_video_url(url):
    hosts = ["youtube.com","rutube.ru","coub.com","vimeo.com","youtu.be"]
    if "watch" in url:
        url = url[:url.find("watch")]+url[url.find("watch")+8:]
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
        return start_page(request)
    profiles = Profile.objects.filter(author=request.user)
    if len(profiles) == 0:
        return redirect('profile_new')
    if request.method == "POST":

        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            #
            #print(request.user.username)
            #user = authenticate(username="Artem", password="coding123")#Тут меняй Artem на Nikita

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
    #post = get_object_or_404(Profile, pk=pk)
    return profile(request)
    #return render(request, 'user_example/profile_detail.html', {'post': post})

def post_detail(request, pk):
    #print(request.user.username)

    post = get_object_or_404(Post, pk=pk)
    profiles = Profile.objects.filter(author=post.author)[0]
    url_profile = profiles.title
    if is_member(request.user,"teacher"):
        return render(request, 'user_example/post_detail.html', {'post': post, "author":profiles.title,"url_prof":url_profile})
    else:
        return render(request, 'user_example/post_detail_stud.html',{'post': post, "author": profiles.title, "url_prof": url_profile})
def index(request):
    return render(request,"user_example/index.html")
def start_page(request):
    posts = Post.objects.filter().order_by('rating')
    posts = posts.reverse()
    lens = len(posts)
    for j in range(lens-1,-1,-1):
        if posts[j].rating < 8:
            posts = posts[:j] + posts[j+1:]

    return render(request,"user_example/start_page.html", {'posts': posts})

def working_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = posts.reverse()
    return render(request,"user_example/working_page.html", {'posts': posts})

def profile(request):
    username1 = request.user.username
    print(username1)
    profiles = Profile.objects.filter(author=request.user)

    if len(profiles) == 0:

        return redirect('profile_new')
        #pass
    else:
        profiles = profiles[0]
        #print(len(profiles))

        #print(is_member(request.user,"group1"))
        if is_member(profiles.author,"teacher"):
            status = "Учитель"
        else:
            status = "Студент"
        posts = Post.objects.filter(author=profiles.author)
        string1 = []
        for j in posts:
            string1.append(str(j.rating))

        return render(request,"user_example/profile.html", {"postss":profiles, "status":status,"values":string1})
def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if(form.is_valid()):
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            #print(username,password)
            user = authenticate(username = username,password = password)
            my_group = Group.objects.get(name='student')
            print(my_group)
            my_group.user_set.add(user)
            login(request,user)
            return redirect("start_page")
    else:

        form = UserCreationForm()
    context = {"form": form}
    return render(request,"registration/register.html",context)





def rating_enter0(request,pk):
    if is_member(request.user, "teacher"):
        post = get_object_or_404(Post, pk=pk)
        post.rating = 0
        post.save()
        print(post.title)

    return redirect('post_detail', pk=post.pk)

def rating_enter1(request,pk):
    if is_member(request.user, "teacher"):
        post = get_object_or_404(Post, pk=pk)
        post.rating = 1
        post.save()
        print(post.title)

    return redirect('post_detail', pk=post.pk)
def rating_enter2(request,pk):
    if is_member(request.user, "teacher"):
        post = get_object_or_404(Post, pk=pk)
        post.rating = 2
        post.save()
        print(post.title)

    return redirect('post_detail', pk=post.pk)
def rating_enter3(request,pk):
    if is_member(request.user, "teacher"):
        post = get_object_or_404(Post, pk=pk)
        post.rating = 3
        post.save()
        print(post.title)

    return redirect('post_detail', pk=post.pk)
def rating_enter4(request,pk):
    if is_member(request.user, "teacher"):
        post = get_object_or_404(Post, pk=pk)
        post.rating = 4
        post.save()
        print(post.title)

    return redirect('post_detail', pk=post.pk)
def rating_enter5(request,pk):
    if is_member(request.user, "teacher"):
        post = get_object_or_404(Post, pk=pk)
        post.rating = 5
        post.save()
        print(post.title)

    return redirect('post_detail', pk=post.pk)
def rating_enter6(request,pk):
    if is_member(request.user, "teacher"):
        post = get_object_or_404(Post, pk=pk)
        post.rating = 6
        post.save()
        print(post.title)

    return redirect('post_detail', pk=post.pk)
def rating_enter7(request,pk):
    if is_member(request.user, "teacher"):
        post = get_object_or_404(Post, pk=pk)
        post.rating = 7
        post.save()
        print(post.title)

    return redirect('post_detail', pk=post.pk)
def rating_enter8(request,pk):
    if is_member(request.user, "teacher"):
        post = get_object_or_404(Post, pk=pk)
        post.rating = 8
        post.save()
        print(post.title)

    return redirect('post_detail', pk=post.pk)
def rating_enter9(request,pk):
    if is_member(request.user, "teacher"):
        post = get_object_or_404(Post, pk=pk)
        post.rating = 9
        post.save()
        print(post.title)

    return redirect('post_detail', pk=post.pk)
def rating_enter10(request,pk):
    if is_member(request.user, "teacher"):
        post = get_object_or_404(Post, pk=pk)
        post.rating = 10
        post.save()
        print(post.title)

    return redirect('post_detail', pk=post.pk)




def task_page(request):
    posts = Task.objects.filter().order_by("published_date")
    posts = posts.reverse()


    if is_member(request.user, "teacher"):
        return render(request, "user_example/Task_page.html", {'posts': posts})
    else:
        return render(request, "user_example/Task_page_stud.html", {'posts': posts})







def task_detail(request, pk):
    #print(request.user.username)

    post = get_object_or_404(Task, pk=pk)
    return render(request, 'user_example/task_detail.html', {'post': post})






def task_new(request):
    if not request.user.is_authenticated or (not is_member(request.user, "teacher")):
        return task_page(request)
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            #
            #print(request.user.username)
            #user = authenticate(username="Artem", password="coding123")#Тут меняй Artem на Nikita

            if not request.user.is_authenticated:
                task_page(request)
            post.author = request.user

            post.published_date = timezone.now()
            post.save()
            return redirect('task_detail', pk=post.pk)
    else:
        form = TaskForm()
    return render(request, 'user_example/task_edit.html', {'form': form})








def my_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        #print(form.errors)

        if (form.is_valid()):

            form.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(username=username, password=password)
            if user is not None:

                login(request, user)
                return redirect("index")


            else:

                return redirect("index")
    else:
        form = UserCreationForm(request.POST)
    context = {"form": form}
    return render(request,"registration/ls.html",context)

