from django.contrib import admin

from .models import Article,Tag,Scope
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

class ScopeInlineFormSet(BaseInlineFormSet) :
    def clean(self):
        main_count = 0
        for form in self.forms :
            if form.cleaned_data and not form.cleaned_data.get("DELETE") :
                if form.cleaned_data.get("is_main") :
                    main_count += 1
        if main_count == 0 :
            raise ValidationError("Необходимо указать основной раздел для статьи")
        elif main_count > 1 :
            raise ValidationError("Основным разделом может быть только один раздел")
        return super().clean()

class ScopeInline(admin.TabularInline) :
    model = Scope
    formset = ScopeInlineFormSet
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin) :
    pass