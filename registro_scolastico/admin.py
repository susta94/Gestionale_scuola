from django.contrib import admin
from registro_scolastico.models import *


 # Questa dicitura mette ("registra") il model nell'admin senza particolari decorazioni o specifiche
admin.site.register(Materia)
admin.site.register(Voto)
admin.site.register(Aula)


# Questo è un "decoratore", vedremo più avanti. Agisce ("decora") sulla prima classe che trova a capo
# dopo sé stesso. La classe definisce "la pagina di admin" e accetta parametri vari predefiniti per spiegare a django come la vuoi
# Tra parentesi va il modello a cui fa riferimento la classe che viene "decorata".
@admin.register(Studente)


class StudenteAdmin(admin.ModelAdmin): # eredità da ModelAdmin, che è la generica idea di pagina di admin in Django
    # la classe ha parametri predefiniti vuoti da sovrascrivere. Solitamente sono elenchi di colonne (fields) rappresentati in liste o tuple


    list_display = ('nome', 'cognome', 'email')  # quali campi si vedono nella tabella di admin
    search_fields = ('nome', 'cognome',)  # quali campi sono "cercabili" dalla casella ricerca (disattivata se non presente)
    ordering = ('cognome',)    # quale campo usare per l'ordinamento degli elementi nella pagina di default, se non c'è usa quello dopo


@admin.register(Professore)

class ProfessoreAdmin(admin.ModelAdmin):

    list_display = ('nome', 'cognome', 'email')
    search_fields = ('nome', 'cognome')
    ordering = ('cognome',)