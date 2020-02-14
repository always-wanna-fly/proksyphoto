from django.db import models


class Subscriber(models.Model):

    call_number = models.CharField("Номер телефону",max_length=128)
    name = models.CharField("Ім'я", max_length=128)
    message = models.CharField('Повідомлення', max_length=128)
    event_date =models.CharField('Час та дата фотосесії', max_length=128)

    def __str__(self):
        return "Пользователь %s %s" % (self.name, self.call_number,)

    class Meta:
        verbose_name = 'Запит'
        verbose_name_plural = 'Запити на фотосесію'