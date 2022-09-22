from statistics import mode
from django.db import models

# Create your models here.
class Posts(models.Model):
    post_descr = models.IntegerChoices(primary_key=True, max_length=128, db_index=True)

    def __str__(self):
        return self.post_descr


class Users(models.Model):
    usr_id  = models.IntegerField(primary_key=True, serialize=True)
    usr_fio = models.CharField(max_length=128, blank=False)
    usr_sex = models.CharField(max_length=1)
    usr_post = models.ForeignKey('Posts', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.usr_fio