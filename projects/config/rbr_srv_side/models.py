from django.db import models

class Server(models.Model):

    name = models.CharField('name', max_length=255, default='name')
    ip_address = models.GenericIPAddressField('ip_address', max_length=16, default='0.0.0.0')
    description = models.TextField('description', max_length=255, default='no_description')
    server_is_active = models.BooleanField(default=False)
    data_active = models.CharField('data_active', max_length=2000, default='data_active')

    class Meta:
        managed = True
        verbose_name = 'Server'
