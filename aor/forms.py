from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext as _
from registration.forms import RegistrationFormUniqueEmail
from captcha.fields import CaptchaField

class RegistrationFormCaptcha(RegistrationFormUniqueEmail):
    captcha = CaptchaField(label=_('Captcha'),
        help_text=_('Enter text from captcha image'))

class AuthenticationFormCaptcha(AuthenticationForm):
    captcha = CaptchaField(label=_('Captcha'),
        help_text=_('Enter text from captcha image'))
