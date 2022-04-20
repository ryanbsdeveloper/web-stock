from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Sum
from produtos.models import EstoqueModel
from .forms import EstoqueForm
from inicio.models import UserModel
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin


def DelProduto(request, id):
    produto = get_object_or_404(EstoqueModel, pk=id)
    produto.delete()
    return redirect('produtos')


class EditarView(LoginRequiredMixin, View):
    template_name = 'detalhe.html'

    def setup(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().setup(request, *args, **kwargs)

        id = kwargs['id']
        self.obj = get_object_or_404(EstoqueModel, pk=id)
        self.contexto = {
            'produto': self.obj,
            'form': EstoqueForm(instance=self.obj)
        }
        super().setup(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = EstoqueForm(request.POST, instance=self.obj)
        
        if form.is_valid():
            form.save()
            return redirect('produtos')
        return render(request, self.template_name, self.contexto)


class DashBoardView(LoginRequiredMixin, View):
    template_name = 'dash.html'

    def setup(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().setup(request, *args, **kwargs)

        self.token_valido_ou_n = UserModel.objects.get(
            usuario=request.user).token
            
        user = EstoqueModel.objects.filter(usuario=request.user)
        total_em_estoque = user.aggregate(Sum('quantidade'))
        total_em_estoque = total_em_estoque['quantidade__sum']
        valores = user.aggregate(Sum('preco'))
        valores = valores['preco__sum'] 
        if not valores or not total_em_estoque:
            valores = 0
            total_em_estoque = 1
            media_valor = 1
            valores_total = 0
        else:
            valores_total = valores * total_em_estoque
            media_valor = valores / user.count()

        self.contexto = {
            'produtos': user,
            'valor_total': round(valores_total, 2),
            'media_valor': round(media_valor),
            'total_estoque': total_em_estoque,
        }
        super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if not self.token_valido_ou_n:
            t = Token.objects.get_or_create(user=request.user)[0]
            # enviando email
            send_mail(
                'Verificação rbs',
                f'''
                    A equipe RBS agradece sua inscrição :) 
                    Token de verificação: {t}
                    *obs:Esse Token é para acesso externo do servidor.''',
                f'{settings.EMAIL_HOST_USER}',
                [f'{request.user.email}'], fail_silently=False)

            return redirect('auth')

        return render(request, self.template_name, self.contexto)


class ProdutosView(LoginRequiredMixin, View):
    template_name = 'estoque.html'

    def setup(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().setup(request, *args, **kwargs)

        self.contexto = {
            'produtos': EstoqueModel.objects.order_by('-created_at').filter(usuario=request.user),
            'form': EstoqueForm(request.POST, request.FILES)
        }
        super().setup(request, *args, **kwargs)


    def get(self, request):
        busca = request.GET.get('busca')
        if busca:
            self.contexto = {
                'produtos': EstoqueModel.objects.order_by('-created_at').filter(usuario=request.user, nome_produto__contains=busca),
                'form': EstoqueForm(request.POST, request.FILES)
            } 
        return render(request, self.template_name, self.contexto)

    def post(self, request):
        form = EstoqueForm(request.POST, request.FILES)

        if form.is_valid():
            produto = form.save(commit=False)
            produto.usuario = request.user
            produto.save()
            return redirect('produtos')
        else:
            print(':)', form.errors)
            messages.error(
                request, 'Preencha o formulário, e tente novamente!')
            return redirect('produtos')


