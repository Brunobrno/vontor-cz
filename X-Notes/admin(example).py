from django.contrib import admin
from .models import MyModel  # Importuj modely

# Příklad přizpůsobení zobrazení modelu v administrátorské sekci
class MyModelAdmin(admin.ModelAdmin):
    # Určují se pole, která se zobrazí v seznamu (list view)
    list_display = ('field1', 'field2', 'field3')  
    # Určuje, podle kterých polí lze vyhledávat
    search_fields = ('field1', 'field2')  
    # Aktivuje filtrování podle hodnoty pole v pravém postranním panelu
    list_filter = ('field1', 'field2')  
    # Určuje pole, která se zobrazí ve formuláři při detailním pohledu na model
    fields = ('field1', 'field2', 'field3')  
    # Definuje rozložení polí ve formuláři
    fieldsets = (
        (None, {
            'fields': ('field1', 'field2'),
        }),
        ('Další informace', {
            'classes': ('collapse',),
            'fields': ('field3',),
        }),
    )
    # Nastavuje výchozí řazení záznamů při jejich zobrazení
    ordering = ('field1',)  
    # Určuje počet záznamů zobrazených na jedné stránce
    list_per_page = 10  
    # Definuje akce dostupné pro vybrané objekty
    actions = ['custom_action']

    # Příklad vlastní akce
    def custom_action(self, request, queryset):
        # Vlastní logika pro akci
        queryset.update(field1='Updated Value')

# Registrování modelu s vlastními nastaveními administrátorského rozhraní
admin.site.register(MyModel, MyModelAdmin)
