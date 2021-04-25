from django.db.models import Model
from django.db.models.fields import CharField, IntegerField


class Lead(Model):
    first_name = CharField(max_length= 20)
    last_name = CharField(max_length= 20)
    age = IntegerField(default=0)
