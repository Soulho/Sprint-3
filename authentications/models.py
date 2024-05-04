from django.db import models
from users.models import User

class Authentications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    value = models.FloatField(null=True, blank=True, default=None)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{"user": %s, "dateTime": %s}' % (self.user.login, self.dateTime)
    
    def toJson(self):
        auth = {
            'id': self.id,
            'user': self.user.login,
            'value': self.value,
            'dateTime': self.dateTime,
        }
        return auth
