from django.contrib import admin
from . models import Acting, Profissional, Status, Project, TeamControl

class ActingAdmin(admin.ModelAdmin):
    fields = ('name_acting',)
    list_display = ('name_acting','created_at','update_at')

class ProfissionalAdmin(admin.ModelAdmin):
    fields = ('nome','control_acting','photo')
    list_display = ('nome','control_acting','photo','created_at','update_at')

class StatusAdmin(admin.ModelAdmin):
    fields = ('nome_status',)
    list_display = ('nome_status','created_at','update_at')

class ProjectAdmin(admin.ModelAdmin):
    fields = ('proj_name',)
    list_display = ('proj_name','created_at','update_at')

class TeamControlAdmin(admin.ModelAdmin):
    fields = ('control_nome','control_acting','control_proj1','control_status1','control_proj2','control_status2','control_proj3','control_status3','control_proj4','control_status4','control_proj5','control_status5','control_proj6','control_status6','control_obs')
    list_display = ('control_nome','control_acting','control_proj1','control_status1','control_proj2','control_status2','control_proj3','control_status3','control_proj4','control_status4','control_proj5','control_status5','control_proj6','control_status6','created_at','update_at')


admin.site.register(Acting, ActingAdmin)
admin.site.register(Profissional, ProfissionalAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(TeamControl, TeamControlAdmin)

