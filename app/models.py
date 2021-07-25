from django.db import models
from account.models import Account
from django_editorjs import EditorJsField
from pytils.translit import slugify


class Geniral_Topics(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Тему'
        verbose_name_plural='Темы'

    def save(self, *args, **kwargs): # new
        self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

class Topics(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    geniral_topic = models.ForeignKey(Geniral_Topics, on_delete=models.CASCADE, verbose_name='Тип статьи', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=False,  verbose_name='URL')
    english_name = models.SlugField(max_length=255, unique=False,  verbose_name='englishName')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs): # new
        self.english_name = slugify(self.name)

        return super().save(*args, **kwargs)

class UserAccess(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='пользователь', blank=True, null=True)
    topics = models.ForeignKey(Topics, on_delete=models.CASCADE, verbose_name='топик', blank=True, null=True)




class Lections(models.Model):
    title = models.CharField(max_length=60, unique=True)

    body = EditorJsField(editorjs_config={
        "tools": {
            "Image": {
                "config": {
                    "endpoints": {
                        "byFile": 'imageUpload/',
                        "byURL": 'imageUpload',
                    },
                    "additionalRequestHeaders": [{"Content-Type": 'multipart/form-data'}]
                }
            },
            "Attaches": {
                "config": {
                    "endpoint": 'fileUpload/'
                }
            }
        }
    })
    question = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=False, verbose_name='slug')
    topics = models.ForeignKey(Topics, on_delete=models.CASCADE, verbose_name='топик', blank=True, null=True)


    def save(self, *args, **kwargs): # new
        self.slug = slugify(self.title)

        return super().save(*args, **kwargs)


class UserResults(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='пользователь', blank=True, null=True)
    lection = models.ForeignKey(Lections, on_delete=models.CASCADE, verbose_name='лекция', blank=True, null=True)
    score = models.IntegerField()
    max_score = models.IntegerField()
    slug = models.SlugField(max_length=255, unique=False, verbose_name='slug')
    sluguser = models.SlugField(max_length=255, unique=False, verbose_name='slug user')
