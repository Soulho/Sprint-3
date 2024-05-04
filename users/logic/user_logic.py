from ..models import User

def get_users():
    queryset = User.objects.all()
    return (queryset)

def get_user_by_login(login):
    queryset = User.objects.filter(login=login)
    return (queryset)