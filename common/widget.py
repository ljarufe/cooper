# -*- coding: utf-8 -*-

'''
Created on 06/08/2010

@author: mauricio
'''

from django import forms
from django.forms import widgets
from django.conf import settings
from django.utils.safestring import mark_safe


# TODO: Hay un error con jquery en el admin
class Markitup(widgets.Textarea):
    """
    Markitup widget
    """
    class Media:
        js = (
          '%sjs/common/jquery-1.4.2.js' % settings.MEDIA_URL,
          '%smarkitup/markitup/jquery.markitup.js' % settings.MEDIA_URL,
          '%smarkitup/markitup/sets/html/set.js' % settings.MEDIA_URL,
          )
        css = {
           'screen':(
                '%smarkitup/markitup/skins/simple/style.css' % settings.MEDIA_URL,
                '%smarkitup/markitup/sets/html/style.css' % settings.MEDIA_URL,
                 )
           }


class ColorPickerWidget(forms.TextInput):
    class Media:
        css = {
            'all': (
                '%scolorPicker/colorPicker.css' % settings.MEDIA_URL,
            )
        }
        js = (
            '%sjs/common/jquery-1.4.2.js' % settings.MEDIA_URL,
            '%scolorPicker/jquery.colorPicker.js' % settings.MEDIA_URL,
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(ColorPickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        rendered = super(ColorPickerWidget, self).render(name, value, attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
            $('#id_%s').colorPicker();
            </script>''' % name)


