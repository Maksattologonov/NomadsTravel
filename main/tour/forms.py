from django import forms

from tour.models import TourDay
from django.urls import reverse
from django.utils.safestring import mark_safe


class TourDayForm(forms.ModelForm):
    class Meta:
        model = TourDay
        fields = '__all__'

    weather_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.id:
            self.fields['weather'].widget.attrs.update({'readonly': True})
            self.fields['weather'].help_text = self.generate_weather_button(self.instance)

    def generate_weather_button(self, obj):
        if obj.id:
            url = reverse('admin:generate-weather', args=[obj.id])
            return mark_safe(
                f'<a class="button" href="{url}" '
                f'style="margin-left: 10px; display: inline-block;">🔄 Генерация погоды</a>'
            )
        return "Сохраните запись, чтобы сгенерировать погоду"