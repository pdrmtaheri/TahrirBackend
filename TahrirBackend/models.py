from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class PersianWord(models.Model):
    word = models.CharField(max_length=50)


class EnglishWord(models.Model):
    word = models.CharField(max_length=50)


class Comment(models.Model):
    comment = models.TextField()
    submitter_name = models.CharField(max_length=50)

    rating = models.PositiveSmallIntegerField()

    translation_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    translation_obj_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('translation_ct', 'translation_obj_id')


class FaToEnTranslation(models.Model):
    source = models.ForeignKey(PersianWord, on_delete=models.CASCADE)
    destination = models.ForeignKey(EnglishWord, on_delete=models.CASCADE)

    verified = models.BooleanField(default=False)
    submitter_name = models.CharField(max_length=50)

    comments = GenericRelation(Comment)


class EnToFaTranslation(models.Model):
    source = models.ForeignKey(EnglishWord, on_delete=models.CASCADE)
    destination = models.ForeignKey(PersianWord, on_delete=models.CASCADE)

    verified = models.BooleanField(default=False)
    submitter_name = models.CharField(max_length=50)

    comments = GenericRelation(Comment)
