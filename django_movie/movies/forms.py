from django import forms

from .models import Reviews, Reitng, ReitngStar


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=ReitngStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Reitng
        fields = ('star', )
