import factory
from .models import User


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User



    email = 'vaspav@vaspav.com'
    username = 'vaspav'
    # password --> nastavljen kot user.set_passwrod = 'medomedo'
    is_superuser = True
    is_staff = True
    is_active = True
