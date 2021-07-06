import faker
import random
from .models import *

fake = faker.Faker('it')


def check_aula(l=None):
    if l is None:
        l = list(Aula.objects.all())
    a = random.choice(l)
    if a.alunni.all().count() <= 20:
        return a
    else:
        l.remove(a)
        check_aula(l)

n_alunni=4
def crea_falso_alunno(n_alunni):
    for i in range(n_alunni):
        falso_studente = Studente.objects.create(
        nome=fake.first_name(),
        cognome=fake.last_name(),
        email=fake.email(),
        )
        for a in range(4):
            falso_studente.competenze.add(random.choice(Materia.objects.all()))

        falso_studente.classe = check_aula()

        falso_studente.save()
        print(f'alunno: {falso_studente}')


def crea_falso_prof(n_prof):
    for i in range(n_prof):
        falso_prof = Professore.objects.create(
            nome=fake.first_name(),
            cognome=fake.last_name(),
            email=fake.email(),
        )
        falso_prof.insegnamenti.add(random.choice(Materia.objects.all()))

        falso_prof.classe = check_aula()

        falso_prof.save()
        print(f'prof: {falso_prof}')


def crea_falsa_sezione(n_sezioni):
    sezioni = Aula.SEZIONI_CHOICES
    anno = Aula.ANNI_CHOICES
    for i in range(n_sezioni):
        for j in range(5):
            aula_falsa = Aula.objects.create(sezione=sezioni[i][0], anno=anno[j][0])
            print(f'ho creato l\'aula: {aula_falsa}')



def creazione(a,b,c):
    crea_falsa_sezione(n_sezioni=a)
    crea_falso_prof(n_prof=b)
    crea_falso_alunno(n_alunni=c)
