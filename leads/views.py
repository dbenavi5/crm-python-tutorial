from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

class LandingPageViews(generic.TemplateView):
    template_name='landing.html'

def landing_page(request):
    return render(request, 'landing.html')

class LeadPageViews(generic.ListView):
    template_name='leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'

def lead_list(request):
    leads = Lead.objects.all()
    context= {
        'leads': leads
    }
    return render(request, "leads/lead_list.html", context)


class LeadDetailViews(generic.DetailView):
    template_name='leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'
    
def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)

class LeadCreateViews(generic.CreateView):
    template_name='leads/lead_create.html'
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse('leads:lead-list')
    
    def form_valid(self, form):
        #TODO: send email
        send_mail(
            subject='A new lead has been created',
            message='Go to site to see new lead',
            from_email='test@example.com',
            recipient_list=['test2@example.com']
        )
        return super(LeadCreateViews, self).form_valid(form)
    
def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context={
        "form":form,
    }
    return render(request, "leads/lead_create.html",context)

class LeadUpdateViews(generic.UpdateView):
    template_name='leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse('leads:lead-list')

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            lead.save()
            return redirect('/leads')
    context = {
        'lead': lead,
        'form':  form,
    }
    
    return render(request, 'leads/lead_update.html', context)

class LeadDeleteViews(generic.DeleteView):
    template_name='leads/lead_delete.html'
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse('leads:lead-list')
    
def lead_delete(request, pk):
    lead = Lead.objects.get(pk=pk)
    lead.delete()
    return redirect('/leads')