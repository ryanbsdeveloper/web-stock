from django.db import models
<<<<<<< HEAD
from phonenumber_field.modelfields import PhoneNumberField


=======
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

>>>>>>> 92e95a22d24feb637e573bff7181e3cb8572e420
class UserModel(models.Model):
    usuario = models.CharField(max_length=50, verbose_name='Usuário')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    senha = models.CharField(max_length=50, verbose_name='Senha')
    telefone = PhoneNumberField(blank=True, null=True)
<<<<<<< HEAD
    token = models.BooleanField(
        verbose_name='Verificação do token', default=False)
    date = models.DateTimeField(auto_now_add=True,  null=True)
=======
    token = models.BooleanField(verbose_name='Verificação do token', default=False)
    created_at = models.DateTimeField(default=datetime.now,  null=True)
>>>>>>> 92e95a22d24feb637e573bff7181e3cb8572e420

    def __str__(self) -> str:
        return self.usuario

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
