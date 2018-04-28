from django.db import models
import datetime

class Pessoa(models.Model):
    nome    = models.CharField("Nome",           max_length=100)
    slug    = models.CharField("slug",           max_length=100)
    apelido = models.CharField("Apelido",        max_length=20)
    login   = models.CharField("Usuário/e-mail", max_length=300)
    senha   = models.CharField("Senha",          max_length=12)

    class Meta:
        verbose_name        = "Pessoa"
        verbose_name_plural = "Pessoas"
        ordering            = ['nome']

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

    """
    metaAtual(pessoa)
    =================
    Retorna a primeira meta de uma pessoa com data maior ou igual ao dia de hoje.
    """
    @staticmethod
    def metaAtual(pessoa):
        metas = Meta.objects.filter(pessoa=pessoa, data__gte=datetime.datetime.now()).order_by('data')
        try:
            return metas[0]
        except:
            return None

    """
    metasVigentes(pessoa)
    =================
    Retorna todas as metas de uma pessoa com data maior ou igual ao dia de hoje.
    """
    @staticmethod
    def metasVigentes(pessoa):
        metas = Meta.objects.filter(pessoa=pessoa, data__gte=datetime.datetime.now()).order_by('data')
        try:
            return metas
        except:
            return None

    """
    metasPessoa(pessoa)

    retorna todas as metas de uma pessoa ordenadas em ordem crescente de data.
    """
    @staticmethod
    def metasPessoa(pessoa):
        try:
            return Meta.objects.filter(pessoa=pessoa, data__gte=datetime.datetime.now()).order_by('data')
        except:
            return None

    def __str__(self):
        return str(self.peso)

class Peso(models.Model):
    data = models.DateTimeField("Data da Pesagem", default=datetime.datetime.today())
    peso = models.DecimalField("Peso", decimal_places=1, max_digits=5)

    pessoa = models.ForeignKey('registro.Pessoa', verbose_name="Pessoa", on_delete=models.CASCADE)

    descricao = models.TextField("Observações", blank=True)


    class Meta:
        verbose_name = 'Peso'
        verbose_name_plural = 'Pesos'
        ordering = ['-data']

    def __str__(self):
        return str(self.peso)
