from django import forms
# from apps.index.models import Tasks
from ckeditor.widgets import CKEditorWidget
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill


class TasksForm(forms.Form):
    title = forms.CharField(required=True, max_length=20)
    describe = forms.CharField(widget=CKEditorWidget(config_name='my_config'))
    price = forms.IntegerField(required=True)
    # to_time = forms.DateTimeField()
    image = ProcessedImageField(spec_id='myapp:profile:avatar_thumbnail',
                                processors=[ResizeToFill(220, 150)],
                                format='JPEG',
                                options={'quality': 90},
                                required=False,
                                allow_empty_file=False)
