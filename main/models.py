from django.db import models

# Create your models here.
class Task(models.Model):
    title =  models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    IMPORTANCE_TYPES = (
        (1, 'Высокая'),
        (2, 'Средняя'),
        (3, 'Низкая')
    )
    importance_type = models.IntegerField(verbose_name='Важность', default=2, choices=IMPORTANCE_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
