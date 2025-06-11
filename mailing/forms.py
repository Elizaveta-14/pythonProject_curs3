
from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField, ModelForm

from .models import AttemptMailing, Mailing, Message, ReceiveMail


class StyleFormMixin:
    """Миксин для стилизации полей формы"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class EmailForm(forms.Form):
    """Форма для отправки email-сообщений"""
    subject = forms.CharField(max_length=255, label="Тема письма")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")
    recipients = forms.CharField(
        widget=forms.Textarea, label="Получатели (через запятую)"
    )


class MailingForm(StyleFormMixin, ModelForm):
    """Форма для создания и редактирования рассылок"""
    class Meta:
        model = Message
        fields = "__all__"


class MessageForm(StyleFormMixin, ModelForm):
    """Форма для создания и редактирования сообщений"""
    class Meta:

        model = Message
        fields = "__all__"


class ReceiveMailForm(StyleFormMixin, ModelForm):
    """Форма для создания и редактирования полученных писем"""
    class Meta:

        model = ReceiveMail
        fields = "__all__"
        exclude = ("can_blocking_client", "owner")


class ReceiveMailModeratorForm(StyleFormMixin, ModelForm):
    """Форма для модераторов для управления полученными письмами"""
    class Meta:

        model = ReceiveMail
        fields = "__all__"


class MailingModeratorForm(StyleFormMixin, ModelForm):
    """Форма для модераторов для управления рассылками"""
    class Meta:
        model = Mailing
        fields = "__all__"
