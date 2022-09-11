from django import forms
from .models import Review



class ReviewForm(forms.ModelForm):
    """Form definition for Review."""

    class Meta:
        """Meta definition for Reviewform."""

        model = Review
        fields = ['image','name','job_description','review',]
        labels = {
            'image':''
        }
        
        def __init__(self, *args, **kwargs):
            super(ReviewForm, self).__init__(*args, **kwargs)

            self.fields['image'].widget.attrs['required'] = 'required'
            self.fields['name'].widget.attrs['required'] = 'required'
            self.fields['job_description'].widget.attrs['required'] = 'required'
            self.fields['review'].widget.attrs['required'] = 'required'
        
