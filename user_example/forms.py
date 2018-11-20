from django import forms

from .models import Post
from .models import Profile
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',"image")

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ("image",)