from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class UserModel(models.Model):
    usuario = models.CharField(max_length=50, verbose_name='Usuário')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    senha = models.CharField(max_length=50, verbose_name='Senha')
    telefone = PhoneNumberField(blank=True, null=True)
    token = models.BooleanField(verbose_name='Verificação do token', default=False)
    created_at = models.DateTimeField(auto_now_add=True,  null=True)

    def __str__(self) -> str:
        return self.usuario

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
