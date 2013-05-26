from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import ugettext as _
from pybb.forms import EditProfileForm
from pybb.models import Post, Topic
from pybb.permissions import perms
from registration.forms import RegistrationFormUniqueEmail
from captcha.fields import CaptchaField
from profiles.models import Profile


class RegistrationFormCaptcha(RegistrationFormUniqueEmail):
    captcha = CaptchaField(label=_('Captcha'),
        help_text=_('Enter text from captcha image'))


class AuthenticationFormCaptcha(AuthenticationForm):
    captcha = CaptchaField(label=_('Captcha'),
        help_text=_('Enter text from captcha image'))


class AORProfileForm(EditProfileForm):
    class Meta:
        model = Profile
        fields = ('signature', 'date_show_type', 'show_signatures', 'theme', 'time_zone',
                  'language', 'avatar', 'icq', 'skype', 'jabber', 'site', 'interests')

    signature = forms.CharField(widget=forms.Textarea, label=_('Signature'),
        required=False)


class SearchForm(forms.Form):
    q = forms.CharField()


class MovePostForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(MovePostForm, self).__init__(*args, **kwargs)
        self.fields['topic'].required = True
        self.fields['topic'].queryset = perms.filter_topics(user, Topic.objects.filter(closed=False))\
            .select_related('forum').order_by('forum', 'forum__name', 'name')

    class Meta:
        model = Post
        fields = ['topic', ]