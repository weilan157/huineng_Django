from django import forms
from django.forms import Select, NumberInput
from django.template.defaultfilters import striptags

from .models import Comment


class CommentForm(forms.ModelForm):
    # honeypot = forms.CharField(required=False,
                               # label='If you enter anything in this field, you comment will be treated as spam!')

    class Meta:
        model = Comment
        # fields = ('content', )
        fields = ('content', 'parent', 'content_type', 'object_id')
        widgets = {'parent': Select(attrs={'cols': 90, 'rows': 90, 'style': 'display:none'}),
                   'content_type': Select(attrs={'cols': 19, 'rows': 19, 'style': 'display:none'}),
                   'object_id': NumberInput(attrs={'cols': 19, 'rows': 19, 'style': 'display:none'})}

    def clean_content(self):
        """
        检查content字段是否为空
        """
        value = self.cleaned_data['content']
        if striptags(value).replace(' ', '').replace('&nbsp;', '') == '' and '<img' not in value:
            self.add_error('content', '评论内容不能为空~')
        return value
