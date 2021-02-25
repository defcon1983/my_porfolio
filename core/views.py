from django.shortcuts import render, redirect
from .models import Welcome, Project, Skill, Contact, Social_network, My_data, Error404
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView

from django.views.generic.list import ListView

from .forms import ContactForm
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
# Create your views here.




def send_email(name, email, content):
    html_content = '<h1>HOLA</h1><p>Muchas gracias por averme proporcionado tus datos, en breve me comunicare contigo</p>'
    email = EmailMultiAlternatives(
        'En breve me pondre en contacto con usted',
        'Gracias',
        settings.EMAIL_HOST_USER,
        [email],
        cc=['dragon.troyano.defcon@gmail.com']
    )
    email.attach_alternative(html_content, 'text/html')
    email.send()

def index(request):
    welcome = Welcome.objects.all()
    project = Project.objects.all()
    skill = Skill.objects.all()
    contact = Contact.objects.all()
    social_network = Social_network.objects.all()
    my_data = My_data.objects.all()
    contact_form = ContactForm()

    context = {
        'Welcome': welcome,
        'Project': project,
        'Skill': skill,
        'Contact': contact,
        'Social_network': social_network,
        'My_data': my_data,
        'contact_form': contact_form
    }     
    if request.method == 'POST':
        contact_form= ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            send_email(name, email ,content)
            return redirect(reverse('index')+'?ok')

    return render(request, 'core/index.html', context=context)

def detalles(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "core/detalles.html", {'project':project})

def mis_datos(request, mis_datos_id):
    mis_datos = get_object_or_404(Welcome, id=mis_datos_id)
    return render(request, "core/mis_datos.html", {'mis_datos':mis_datos})
    
def skill_detalles(request, skill_detalles_id):
    data = get_object_or_404(Skill, id=skill_detalles_id)
    return render(request, "core/skill_detalles.html", {'data':data})

class Error404(TemplateView):
    template_name = "core/error404.html"


class Error505(TemplateView):
    template_name = "core/error404.html"

    @classmethod
    def as_error_view(cls):
        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view
