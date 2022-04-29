from django.db import models
from django.contrib.auth import get_user_model


class Acting(models.Model): #Lista de Funções

    name_acting = models.CharField(max_length=255, verbose_name='ÁREA')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_acting


class Profissional(models.Model): #Lista de Funcionários

    nome = models.CharField(max_length=255, verbose_name='NOME')
    control_acting = models.ForeignKey(Acting, on_delete=models.CASCADE, verbose_name='ÁREA')
    photo = models.FileField(upload_to='uploads/photos/', blank=True, null=True, verbose_name='FOTO')
    #user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='USUÁRIO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    
class Status(models.Model): #Status de Atividades

    nome_status = models.CharField(max_length=255, verbose_name='STATUS')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_status

class Project(models.Model): #Status de Atividades

    proj_name = models.CharField(max_length=255, verbose_name='STATUS')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_status


class TeamControl(models.Model): #Tabela de Controle

    control_nome = models.ForeignKey(Profissional, on_delete=models.CASCADE, verbose_name='NOME')
    control_acting = models.ForeignKey(Acting, on_delete=models.CASCADE, verbose_name='FUNÇÃO')
    control_proj1 = models.CharField(max_length=255, verbose_name='PROJETO A')
    control_status1 = models.CharField(max_length=255, verbose_name='STATUS A')
    control_proj2 = models.CharField(max_length=255, verbose_name='PROJETO B')
    control_status2 = models.CharField(max_length=255, verbose_name='STATUS B')
    control_proj3 = models.CharField(max_length=255, verbose_name='PROJETO C')
    control_status3 = models.CharField(max_length=255, verbose_name='STATUS C')
    control_proj4 = models.CharField(max_length=255, verbose_name='PROJETO D')
    control_status4 = models.CharField(max_length=255, verbose_name='STATUS D')
    control_proj5 = models.CharField(max_length=255, verbose_name='PROJETO E')
    control_status5 = models.CharField(max_length=255, verbose_name='STATUS E')
    control_proj6 = models.CharField(max_length=255, verbose_name='PROJETO F')
    control_status6 = models.CharField(max_length=255, verbose_name='STATUS F')
    #control_proj2 = models.CharField(max_length=255, verbose_name='PROJETO B')
    #control_status2 = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='STATUS B')
    control_obs = models.CharField(max_length=255, verbose_name='OBS')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

        
class Upload(models.Model): #Upload de arquivos
    arq = models.FileField(upload_to='uploads/', help_text='localizar Arquivo')
    update_arq = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.arq)




