from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Journal


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def journals_index(request):
    # Assuming you want to retrieve all Journal objects
    journals = Journal.objects.all()

    return render(request, 'journals/index.html', {'journals': journals})

def journals_detail(request, journal_id):
    # Your implementation for displaying details
    pass

    # Pass the journal object to the template
    return render(request, 'journals/journals_detail.html', {'journal': journal})

class JournalCreate(LoginRequiredMixin, CreateView):
    model = Journal
    fields = ['title', 'description', 'date', 'content', 'location']  # Adjust the fields as needed

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    # This inherited method is called when a valid form is being submitted
    def form_valid(self, form):
        # Assign the logged-in user (self.request.user) to the journal entry
        form.instance.user = self.request.user
        # Let the CreateView do its job as usual
        return super().form_valid(form)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


