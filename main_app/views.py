from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Journal, Comment  # Import the Comment model
from .forms import JournalForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def journals_index(request):
    journals = Journal.objects.all()
    return render(request, 'journals/index.html', {'journals': journals})

def journals_detail(request, journal_id):
    journal = get_object_or_404(Journal, pk=journal_id)
    return render(request, 'journals/journals_detail.html', {'journal': journal})

class JournalCreate(LoginRequiredMixin, CreateView):
    model = Journal
    form_class = JournalForm
    template_name = 'journals/journal_form.html'

    def form_valid(self, form):
        print("Form is valid:", form.is_valid())
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        print("get_success_url is called!")
        return reverse('journals_detail', kwargs={'journal_id': self.object.id})

# Add this view for handling comments
def add_comment(request, journal_id):
    journal = get_object_or_404(Journal, pk=journal_id)

    if request.method == 'POST':
        # Handle comment submission
        # Assuming you have a Comment model and a CommentForm
        # Replace CommentForm with your actual form for handling comments
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create and save the comment
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.journal = journal
            comment.save()

    return redirect('journals_detail', journal_id=journal_id)

# Your existing signup function remains unchanged
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def journals_edit(request, journal_id):
    # Your implementation for editing journals
    pass

def journals_delete(request, journal_id):
    # Your implementation for editing journals
    pass