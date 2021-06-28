from django.db import models

class Geniral_Topics(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Тему'
        verbose_name_plural='Темы'

class Topics(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    geniral_topic = models.ForeignKey(Geniral_Topics, on_delete=models.CASCADE, verbose_name='Тип статьи', blank=True, null=True)

    def __str__(self):
        return self.name


class Questions(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE, verbose_name='Тип статьи', blank=True, null=True)

    question = models.CharField(max_length=500, verbose_name='Вопрос')


