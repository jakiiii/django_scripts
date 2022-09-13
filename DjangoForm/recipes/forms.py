from django import forms

from .models import Recipe, RecipeIngredient, RecipeIngredientImage


class RecipeForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    # name = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Recipe name"}))
    # description = forms.CharField(widget=forms.Textarea(attrs={"row": 3}))

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            update_design = {
                "placeholder": f'Recipe {str(field)}',
                "class": 'form-control'
            }
            self.fields[str(field)].widget.attrs.update(update_design)
        # self.fields['name'].widget.attrs.update({'class': 'form-control-2'})
        self.fields['description'].widget.attrs.update({'rows': 2})
        self.fields['directions'].widget.attrs.update({'rows': 4})


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            update_design = {
                "placeholder": f'Recipe {str(field)}',
                "class": 'form-control'
            }
            self.fields[str(field)].widget.attrs.update(update_design)
