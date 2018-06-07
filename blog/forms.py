from django import forms
from .models import Comment
class EmailPostForm(forms.Form):

    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
        widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class':'form-group','placeholder':'enter name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-group','placeholder':'enter email'}))
    comments = forms.CharField(required=False,
                               widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ('name', 'email', 'comments')