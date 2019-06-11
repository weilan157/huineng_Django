from django import forms
from .models import User
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill


class UserinfoForm(forms.Form):
    """从模型继承表单"""
    avatar = ProcessedImageField(spec_id='myapp:profile:avatar_thumbnail',
                                 processors=[ResizeToFill(80, 80)],
                                 format='png',
                                 options={'quality': 80})
    # avatar = forms.ImageField()
    # class Meta:
    #     module = User
    #     fields = ['avatar']
