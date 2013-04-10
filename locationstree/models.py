from django.db import models
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey


class Location(MPTTModel):
    code = models.CharField(_('Code'), max_length=20, unique=True)
    name = models.CharField(_('Name'), max_length=100)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=_('Parent'))
    sort_order = models.IntegerField(_('Sort Order'), default=0)

    class MPTTMeta:
        order_insertion_by = ['sort_order', 'code']

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    def __unicode__(self):
        return self.name
