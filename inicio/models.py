from django.db import models

class UserModel(models.Model):
    usuario = models.CharField(max_length=50, verbose_name='Usuário')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    senha = models.CharField(max_length=50, verbose_name='Senha')
    token = models.BooleanField(verbose_name='Verificação do token', default=False)

    def __str__(self) -> str:
        return self.usuario

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
