from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import ControleProf
#from .forms import ProjectForm, LdProjForm #, SubjectForm, PageTypeForm, DocTypeForm, PageformatForm, DocumentModelForm, EmployeeForm, StatusDocForm, ActionForm #, LdProjForm, CotationForm
from django.contrib import messages

@login_required
def home(request):

    return render(request,'task/index.html')


@login_required
def listaFunc(request):

    '''GET = dict(request.GET)
    if str(GET) == '{}':
        return redirect('/')

    else:

    new_id = str(GET).replace("{'","").replace("': ['']}","")
    proj_id = int(new_id)
    ListDoc = DocumentListProject.objects.all().order_by('id')
    '''

    Controle = ControleProf.objects.all()

    return render(request, 'task/lista-func.html',{'Controle':Controle})