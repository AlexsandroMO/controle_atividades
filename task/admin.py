from django.contrib import admin
from . models import Funcao, Profissional, Disciplina, Status, ControleProf

class FuncaoAdmin(admin.ModelAdmin):
    fields = ('nome_funcao',)
    list_display = ('nome_funcao','created_at','update_at')

class ProfissionalAdmin(admin.ModelAdmin):
    fields = ('nome','controle_func','data_contrato','photo')
    list_display = ('nome','controle_func','data_contrato','photo','created_at','update_at')
    
class DisciplinaAdmin(admin.ModelAdmin):
    fields = ('nome_disciplina',)
    list_display = ('nome_disciplina','created_at','update_at')

class StatusAdmin(admin.ModelAdmin):
    fields = ('nome_status',)
    list_display = ('nome_status','created_at','update_at')

class ControleProfAdmin(admin.ModelAdmin):
    fields = ('controle_nome','controle_func','controle_disc','controle_proj1','controle_proj2','controle_status','controle_obs')
    list_display = ('controle_nome','controle_func','controle_disc','controle_proj1','controle_proj2','controle_status','controle_obs','created_at','update_at')

admin.site.register(Funcao, FuncaoAdmin)
admin.site.register(Profissional, ProfissionalAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(ControleProf, ControleProfAdmin)

