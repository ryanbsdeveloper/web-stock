from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from rest_framework.authtoken.models import Token



class APIView(LoginRequiredMixin, View):
    template_name = 'api.html'

    def setup(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().setup(request, *args, **kwargs)
        
        token = Token.objects.get_or_create(user=request.user)[0]
        self.contexto = {
            'token': token
        }
        super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

