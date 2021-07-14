
# Importiamo models, la classe creata da quelli di Django per rappresentare una tabella di DB, che loro chiamano "modello".
# Ogni model rappresenterà poi LA TABELLA degli oggetti, il loro insieme generico, l'idea di oggetto e non gli oggetti
# stessi o un gruppo di oggetti.
from django.db import models
from django.urls import reverse_lazy


#  OneToOneField    Uno a uno     - univoca                             - informazioni account-->conto in banca
#  ManyToManyField  tanti a tanti - molteplice                          -  materie <---> professori
#  ForeignKey       uno a tanti   - uno da un lato, molti dall'altro    -  auto ---> marchio


# NB: 1to1 è spesso usata in produzione per dividere il carico di lavoro di un qualcosa tra due tabelle quando hai due "set di informazioni"
# che vengono chiamati in momenti diversi anche se potrebbero essere messi nella stessa cosa (ad esempio informazioni di login di un account e il suo storico transazioni)





class Studente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='nome', help_text='nome dello studente', blank=False, null=True)
    cognome = models.CharField(max_length=100, verbose_name='cognome', help_text='cognome dello studente', blank=False, null=True)
    email = models.EmailField(verbose_name='indirizzo email', help_text='contatto mail dello studente', blank=False, null=True)
    # alcuni field come emailfield compiono delle validazioni per assicurarsi che tutta la colonna di dati corrisponda a un determinato formato, per poterci fare determinate operazioni (tipo inviare le mail)
    competenze = models.ManyToManyField('registro_scolastico.Materia', related_name='insegnato_a')
    classe = models.ForeignKey('registro_scolastico.Aula', related_name='alunni', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        # estetismo
        # Questo metodo viene lanciato quando sulla classe viene eseguito un print o quando viene usata come stringa da qualche parte.
        # Può eseguire codice arbitrario ma deve return-are per forza una str
        return self.nome + ' ' + self.cognome

    def get_absolute_url(self):
        return reverse_lazy('dettaglio_studente', args=[str(self.pk)])


    def materia_studiate(self):
        materie = self.competenze.all()
        nomi_materie = materie.values_list('nome', flat=True)
        result = ', '.join(nomi_materie)
        return result

    class Meta:
    # per ora, utile per estetismi
    # Permette di specificare il nome singolare e plurale della classe quando richiamata da django in vari contesti, perlopiù nell'admin
        verbose_name_plural = "Studenti"



class Professore(models.Model):
    nome = models.CharField(max_length=100, verbose_name='nome', help_text='nome del professore', blank=False, null=True)
    cognome = models.CharField(max_length=100, verbose_name='cognome', help_text='cognome del professore', blank=False, null=True, default='')
    email = models.EmailField(verbose_name='indirizzo email', help_text='contatto mail del professore', blank=False, null=True, default='')

    insegnamenti = models.ManyToManyField('registro_scolastico.Materia', related_name='insegnato_da')
    lezioni = models.ManyToManyField('registro_scolastico.Aula', related_name='insegnanti', blank=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.nome + ' ' + self.cognome
    class Meta:
        verbose_name_plural = "Professori"


class Materia(models.Model):
    nome = models.CharField(max_length=100, verbose_name='insegnamento', help_text='nome insegnamento', blank=False, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Materie"

class Voto(models.Model):
    valore = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Voto", help_text="valore del voto")

    stud = models.ForeignKey('registro_scolastico.Studente',verbose_name="Studente",help_text="Studente che ha preso il voto", on_delete=models.CASCADE, related_name='risultati')
    mat = models.ForeignKey('registro_scolastico.Materia', on_delete=models.CASCADE, related_name='voti_presi')

    class Meta:
        verbose_name_plural = "Voti"


class Aula(models.Model):
    import string
    ANNI_CHOICES = [[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']]
    SEZIONI_CHOICES = [(i,i) for i in list(string.ascii_uppercase)]

    sezione = models.CharField(max_length=1, verbose_name='Sezione', choices=SEZIONI_CHOICES)
    anno = models.IntegerField(verbose_name='Anno', choices=ANNI_CHOICES)

    class Meta:
        verbose_name_plural = "Aule"
    def conta_studs(self):
        return self.alunni.all().count()



    def __str__(self):
        return str(self.anno)+str(self.sezione)