from users.models import User
from ..models import Authentications

def get_auths():
    queryset = Authentications.objects.all().order_by('-dateTime')
    return (queryset)

def create_auth(user, value):
    auth = Authentications()
    auth.user = user
    auth.value = value
    auth.save()
    return auth