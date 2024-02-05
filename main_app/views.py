from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Journal, Comment  # Import the Comment model
from .forms import JournalForm, CommentForm, EntryForm


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

def journals_edit(request, journal_id):
    journal = get_object_or_404(Journal, pk=journal_id)
    
    if request.method == 'POST':
        form = JournalForm(request.POST, instance=journal)
        if form.is_valid():
            form.save()
            return redirect('journals_detail', journal_id=journal_id)
    else:
        form = JournalForm(instance=journal)
    
    return render(request, 'journals/journals_edit.html', {'form': form, 'journal': journal})

def journals_delete(request, journal_id):
    # Get the journal to be deleted
    journal = get_object_or_404(Journal, pk=journal_id)

    # Check if the user making the request is the owner of the journal
    if request.user == journal.user:
        # Delete the journal
        journal.delete()

        # Redirect to the journals list page or any other desired URL
        return redirect('journals')

    # If the user is not the owner, you might want to handle this case differently
    # For now, let's redirect them back to the detail page
    return redirect('journals_detail', journal_id=journal_id)

# Add this view for handling comments
def add_comment(request, journal_id):
    journal = get_object_or_404(Journal, pk=journal_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create and save the comment
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.journal = journal
            comment.save()

            return redirect('journals_detail', journal_id=journal_id)
    else:
        # If the request method is not POST, create an instance of the form
        comment_form = CommentForm()

    # Render the detail page with the form
    return render(request, 'journals/journals_detail.html', {'journal': journal, 'comment_form': comment_form})

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
    
def add_entry(request, journal_id):
    journal = get_object_or_404(Journal, pk=journal_id)

    if request.method == 'POST':
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid():
            # Create and save the comment
            entry = entry_form.save(commit=False)
            entry.journal = journal
            entry.save()

            return redirect('journals_detail', journal_id=journal_id)
    else:
        # If the request method is not POST, create an instance of the form
        entry_form = EntryForm()

    # Render the detail page with the form
    return render(request, 'main_app/entry_form.html', {'journal': journal, 'entry_form': entry_form})


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

