from django.core.exceptions import ValidationError
from django.forms.models import ModelChoiceIterator, ModelChoiceField
from django.forms.widgets import Select
from django.utils.encoding import force_unicode
from django.utils.html import escape, conditional_escape
from django.utils.translation import ugettext_lazy as _

from mptt.forms import TreeNodeChoiceField


class JustLeafsLocationField(TreeNodeChoiceField):
    def __init__(self, *args, **kwargs):
        kwargs['widget'] = SelectWithDisabled()
        self.default_error_messages['not_leaf'] = _('Select a valid choice. %(value)s is not one of the available choices.')
        super(JustLeafsLocationField, self).__init__(*args, **kwargs)

    def _get_choices(self):
        if hasattr(self, '_choices'):
            return self._choices
        return GroupedLocationModelChoiceIterator(self)

    choices = property(_get_choices, ModelChoiceField._set_choices)

    def validate(self, value):
        super(JustLeafsLocationField, self).validate(value)
        if not value.is_leaf_node():
            raise ValidationError(self.error_messages['not_leaf'] % {'value': value})


class GroupedLocationModelChoiceIterator(ModelChoiceIterator):
    def __iter__(self):
        if self.field.empty_label is not None:
            yield (u"", self.field.empty_label)

        for location in self.field.queryset:
            label = self.field.label_from_instance(location)
            if location.is_leaf_node():
                yield (location.id, label)
            else:
                yield (location.id, {'label': label, 'disabled': True})


class SelectWithDisabled(Select):
    """
    Subclass of Django's select widget that allows disabling options.
    To disable an option, pass a dict instead of a string for its label,
    of the form: {'label': 'option label', 'disabled': True}
    """
    def render_option(self, selected_choices, option_value, option_label):
        option_value = force_unicode(option_value)
        if (option_value in selected_choices):
            selected_html = u' selected="selected"'
        else:
            selected_html = ''
        disabled_html = ''
        if isinstance(option_label, dict):
            if dict.get(option_label, 'disabled'):
                disabled_html = u' disabled="disabled"'
            option_label = option_label['label']
        return u'<option value="%s"%s%s>%s</option>' % (
            escape(option_value), selected_html, disabled_html,
            conditional_escape(force_unicode(option_label)))
