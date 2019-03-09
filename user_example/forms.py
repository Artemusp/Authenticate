from django import forms

from .models import Post
from .models import Profile
from .models import Task
from .models import Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',"image","video_url", "file")#,"rating"

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ("title","text","image","course","group","direction")

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ("title","text","image", "video_url", "file","file2","file3")


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("text",)