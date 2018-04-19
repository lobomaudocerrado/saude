from django.db import models

class Pessoa(models.Model):
    nome = models.CharField("Nome", max_length=100)
    apelido = models.CharField("Apelido", max_length=20)
    login = models.CharField("Usuário/e-mail", max_length=300)
    senha = models.CharField("Senha", max_length=12)
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Meta(models.Model):
    peso = models.DecimalField("Peso", decimal_places=1, max_digits=5)
    data = models.DateTimeField("até")

    pessoa = models.ForeignKey('registro.Pessoa', verbose_name="Pessoa", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Meta'
        verbose_name_plural = 'Metas'
        ordering = ['-data']

    def __str__(self):
        return str(self.peso)

class Peso(models.Model):
    data = models.DateTimeField("Data da Pesagem", auto_now_add=True)
    peso = models.DecimalField("Peso", decimal_places=1, max_digits=5)

    pessoa = models.ForeignKey('registro.Pessoa', verbose_name="Pessoa", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Peso'
        verbose_name_plural = 'Pesos'
        ordering = ['-data']

    def __str__(self):
        return str(self.peso)
