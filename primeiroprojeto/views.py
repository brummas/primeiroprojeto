
from forms import ContatoForm
from django.contrib import messages
from django.shortcuts import render

def contato(request):
    form = ContatoForm(request.POST)
    
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            
            print('Mensagem enviada')
            print('Nome: ', nome)
            print('E - mail: ', email)
            print('Assunto: ', assunto)
            print('Mensagem: ', mensagem)
            
            messages.success(request, message='E-mail enviado com suesso')
            form= ContatoForm()
            
        else:
            messages.error(request, message='Erro ao enviar')
            
    context = {'form': form}
    return render(request, context, template_name="contato.html")
            
