from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):  
    class Meta:
        model = Comment
        fields = ['content']
        
    content = forms.CharField(widget = forms.Textarea(attrs = {  
    'placeholder': 'Leave your comment here.',  
    'class': 'form-control',  
    'rows': 3  
    }))