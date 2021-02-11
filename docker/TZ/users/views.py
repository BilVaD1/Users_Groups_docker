from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db.models import ProtectedError
from django.contrib import messages
from .models import Users, Groups
from .forms import UsersForm, GroupsForm
from django.views.generic import UpdateView, DeleteView


# Create your views here.


def users_groups(request):
    users = Users.objects.order_by('id')
    groups = Groups.objects.order_by('id')
    data = {
        'users': users,
        'groups': groups
    }
    return render(request, 'users/users_groups.html', data)


class UsersDeleteView(DeleteView):  # Delete page
    model = Users
    success_url = '/'  # Redirect after delete
    template_name = 'users/users-delete.html'


class GroupsDeleteView(DeleteView):  # Delete page
    model = Groups
    success_url = '/'  # Redirect after delete
    template_name = 'users/groups-delete.html'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()

        try:
            self.object.delete()
        except ProtectedError:
            messages.add_message(request, messages.ERROR, 'Can not delete: this group has a user!')
            return redirect('/')

        return HttpResponseRedirect(success_url)


class UsersUpdateView(UpdateView):  # Update page
    model = Users
    template_name = 'users/update.html'
    success_url = '/'
    form_class = UsersForm


class GroupsUpdateView(UpdateView):  # Update page
    model = Groups
    template_name = 'users/update_groups.html'
    success_url = '/'
    form_class = GroupsForm


def create(request):
    error = ''
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():   # Checking validation of form
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверно заполнена'
    form = UsersForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'users/create.html', data)


def create_groups(request):
    error = ''
    if request.method == 'POST':
        form = GroupsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверно заполнена'
    form = GroupsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'users/create_groups.html', data)
