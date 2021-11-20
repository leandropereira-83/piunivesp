from django.db import models

class UC(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    thumb=models.ImageField(upload_to ="thumb_uc")

    def __str__(self) -> str:
        return self.nome

class AtividadeUC(models.Model):
    nome_atividade = models.CharField(max_length=100)
    descricao = models.TextField()
    plano = models.FileField(upload_to = "plano")
    complemento_1= models.FileField (upload_to = "complemento")
    uc = models.ForeignKey(UC, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome_atividade
