from django.views.generic import TemplateView
from .tasks import say_hello
from .models import DemoModel
# Create your views here.


class ShowHelloWorld(TemplateView):
    template_name = 'hello_world.html'

    def get(self, *args, **kwargs):
        res = say_hello.apply()
        print(res.get())
        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demo_content'] = DemoModel.objects.all()
        return context
