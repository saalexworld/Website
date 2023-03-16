from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


# Создание формы необходимо для того чтобы связать объекты на веб-странице с моделью (базой данных)
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles

        widgets = {
            "title": TextInput(attrs={
                'class': "form_control",
                'placeholder': "Note title"
            }),
            "intro": TextInput(attrs={
                'class': "form_control",
                'placeholder': "Introduction"
            }),
            "text_content": Textarea(attrs={
                'class': "form_control",
                'placeholder': "Content"
            }),
            "date": DateTimeInput(attrs={
                'class': "form_control",
                'placeholder': "Date"
            }),
        }
        
        fields = '__all__'
