from django.db import models
from django.contrib.auth import get_user_model


class Funcao(models.Model): #Lista de Funções

    nome_funcao = models.CharField(max_length=255, verbose_name='NOME')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_funcao


class Profissional(models.Model): #Lista de Funcionários

    nome = models.CharField(max_length=255, verbose_name='NOME')
    controle_func = models.ForeignKey(Funcao, on_delete=models.CASCADE, verbose_name='FUNÇÃO')
    data_contrato = models.DateField(blank=True, null=True)
    photo = models.FileField(upload_to='uploads/photos/', blank=True, null=True, verbose_name='FOTO')
    #user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='USUÁRIO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Disciplina(models.Model): #Disciplinas

    nome_disciplina = models.CharField(max_length=255, verbose_name='NOME DISCIPLINA')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_disciplina

    
class Status(models.Model): #Status de Atividades

    nome_status = models.CharField(max_length=255, verbose_name='STATUS')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_status


class ControleProf(models.Model): #Tabela de Controle

    controle_nome = models.ForeignKey(Profissional, on_delete=models.CASCADE, verbose_name='NOME')
    controle_func = models.ForeignKey(Funcao, on_delete=models.CASCADE, verbose_name='FUNÇÃO')
    controle_disc = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='DISCIPLINA')
    #controle_lider = models.ForeignKey(Profissional, on_delete=models.CASCADE, verbose_name='LÍDER')
    controle_proj1 = models.CharField(max_length=255, verbose_name='PROJETO ATUAL')
    controle_proj2 = models.CharField(max_length=255, verbose_name='PROJETO ANTERIOR')
    controle_status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='STATUS')
    controle_obs = models.CharField(max_length=255, verbose_name='OBS')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


        
class Upload(models.Model): #Upload de arquivos
    arq = models.FileField(upload_to='uploads/', help_text='localizar Arquivo')
    update_arq = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.arq)
