from django.forms import ModelForm
from .models import Squirrels


class Form(ModelForm):
    class Meta:
        model = Squirrels
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
