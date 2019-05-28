from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class PersianWord(models.Model):
    word = models.CharField(max_length=50)


class EnglishWord(models.Model):
    word = models.CharField(max_length=50)


class FaToEnTranslation(models.Model):
    source = models.ForeignKey(PersianWord, on_delete=models.CASCADE)
    destination = models.ForeignKey(EnglishWord, on_delete=models.CASCADE)

    rating = models.PositiveSmallIntegerField()
    verified = models.BooleanField(default=False)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)


class EnToFaTranslation(models.Model):
    source = models.ForeignKey(EnglishWord, on_delete=models.CASCADE)
    destination = models.ForeignKey(PersianWord, on_delete=models.CASCADE)

    rating = models.PositiveSmallIntegerField()
    verified = models.BooleanField(default=False)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.TextField()
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)

    translation_ct = models.ForeignKey(ContentType, limit_choices_to=(EnToFaTranslation, FaToEnTranslation),
                                       on_delete=models.CASCADE)
    translation_obj_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('translation_ct', 'translation_obj')
