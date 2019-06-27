from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class PersianWord(models.Model):
    word = models.CharField(max_length=50, unique=True)


class EnglishWord(models.Model):
    word = models.CharField(max_length=50, unique=True)


class Comment(models.Model):
    comment = models.TextField()
    submitter_name = models.CharField(max_length=50)

    rating = models.PositiveSmallIntegerField()

    translation_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    translation_obj_id = models.PositiveIntegerField()
    translation = GenericForeignKey('translation_ct', 'translation_obj_id')


class FaToEnTranslation(models.Model):
    word = models.ForeignKey(PersianWord, on_delete=models.CASCADE)
    translation = models.ForeignKey(EnglishWord, on_delete=models.CASCADE)

    verified = models.BooleanField(default=False)
    submitter_name = models.CharField(max_length=50)

    comments = GenericRelation(Comment)

    class Meta:
        unique_together = ('word', 'translation')


class EnToFaTranslation(models.Model):
    word = models.ForeignKey(EnglishWord, on_delete=models.CASCADE)
    translation = models.ForeignKey(PersianWord, on_delete=models.CASCADE)

    verified = models.BooleanField(default=False)
    submitter_name = models.CharField(max_length=50)

    comments = GenericRelation(Comment)

    class Meta:
        unique_together = ('word', 'translation')
