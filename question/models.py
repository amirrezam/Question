from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone


# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=80,verbose_name="سرتیتر")
    body = models.TextField(verbose_name="بدنه", validators=[MinLengthValidator(30, "متن کوتاه است")])
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
