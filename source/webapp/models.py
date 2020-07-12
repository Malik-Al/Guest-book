from django.db import models


STATUS_ACTIVE = "active"
STATUS_CHOICES = (
    (STATUS_ACTIVE, "Активно"),
    ("blocked", "Заблокировано")
)



class Book(models.Model):
    author = models.CharField(max_length=100, verbose_name='Автор')
    email = models.EmailField(max_length=100, verbose_name='Email')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    status = models.CharField(max_length=40, null=False, blank=False, default=STATUS_ACTIVE,
                              choices=STATUS_CHOICES, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.author