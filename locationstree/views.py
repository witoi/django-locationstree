from django import forms
from django.views.generic import FormView
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Location
from .conf import settings


class DefaultLocationForm(forms.Form):
    location = forms.ModelChoiceField(queryset=Location.objects.all())


class SetUserLocation(FormView):
    template_name = 'locationstree/location_form.html'

    def get_form_class(self):
        return self.kwargs.get('location_form', DefaultLocationForm)

    def form_valid(self, form):
        self.request.session[settings.LOCATIONSTREE_LOCATION_SESSION_NAME] = form.cleaned_data['location'].pk
        if self.request.GET.get('next'):
            return redirect(self.request.GET.get('next'))
        return HttpResponse()

set_user_location = SetUserLocation.as_view()
