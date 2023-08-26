from django.db import models

# Create your models here.

class Post(models.Model):
    date=models.DateField(blank=True,null=True)
    title=models.CharField(max_length=128)
    theme=models.CharField(max_length=128)
    image=models.ImageField(upload_to='imagePost')
    blogPoster=models.CharField(max_length=128,blank=True)
    joinPiece=models.URLField(blank=True)
    
    def __str__(self):
        return f"publication de {self.blogPoster} - le : {self.date} titre : {self.title} "
    
class Service(models.Model):
    name=models.CharField(max_length=90)
    
    def __str__(self):
        return f"service : {self.name}"
    
class Temoignage(models.Model):
    nom=models.CharField(max_length=128)
    contenu=models.TextField()
    profession=models.CharField(max_length=128,blank=True)
    def __str__(self):
        return f"Témoignage de  : {self.nom} - {self.profession}"

class Partner(models.Model):
    site = models.URLField(null=True,blank=True)
    name = models.CharField(max_length=128)
    image = models.ImageField()
    def __str__(self):
        return f"partenaire {self.name}"   
    

class Team(models.Model):
    site=models.URLField(null=True,blank=True)
    nom = models.CharField(max_length=128)
    poste=models.CharField(max_length=128)
    whatsapp=models.CharField(max_length=128,null=True)
    twitter=models.CharField(max_length=128,null=True,blank=True)
    insta=models.CharField(max_length=128,null=True,blank=True)
    facebook=models.CharField(max_length=128,null=True,blank=True)
    photo=models.ImageField(blank=True,upload_to='imagePoste',null=True)
    
    def __str__(self):
        return f"Membre {self.nom} - {self.poste}"
    
class WhaGroup(models.Model):
    Titre=models.CharField(max_length=128)
    description=models.TextField(null=True)
    lien=models.URLField()
    image = models.ImageField()
    def __str__(self):
        return f"Whatsapp {self.Titre}"
    
class FAQ(models.Model):
    question=models.TextField()
    reponse=models.TextField()
    def __str__(self):
        return f"Question : {self.question}"
    
class RendezVous(models.Model):
    email=models.EmailField(null=True,blank=True)
    nom=models.CharField(max_length=128)
    whatsapp=models.CharField(max_length=128)
    ville=models.CharField(max_length=128)
    quartier=models.CharField(max_length=128,blank=True,null=True)

    date=models.DateField()
    heure=models.TimeField(null=True,blank=True)
    status=models.CharField(max_length=128,null=True,blank=True)
    Message=models.TextField(null=True,blank=True)
    def __str__(self):
        return f" {self.ville} - {self.quartier} - Demande de rendez-vous de : {self.nom} - le {self.date} à {self.heure} : {self.whatsapp}"

class Consultation(models.Model):
    email=models.EmailField(null=True,blank=True)
    quartier=models.CharField(max_length=128,blank=True,null=True)
    whatsapp=models.CharField(max_length=13)
    nom=models.CharField(max_length=128)
    nomAnimal=models.CharField(max_length=128,blank=True,null=True)
    ville=models.CharField(max_length=128)
    date=models.DateField(null=True,blank=True)
    sexe=models.CharField(max_length=128,blank=True)
    age=models.CharField(max_length=128,null=True)
    espece=models.CharField(max_length=128)
    race=models.CharField(max_length=128,null=True,blank=True)
    Vacc=models.CharField(max_length=128,null=True,blank=True)
    couleur=models.CharField(max_length=128,null=True,blank=True)
    Motif=models.TextField()
    def __str__(self):
        return f" {self.ville}- {self.quartier} - Demande de diagnostique de : {self.nom} - pour {self.espece} - {self.whatsapp}"
    

class informations (models.Model):
    lieu=models.CharField(max_length=128)
    email=models.EmailField()
    numéro=models.CharField(max_length=128)
    lienVideoTuto=models.URLField(null=True)
    lienVideoTravail=models.URLField(null=True)
    twitter=models.URLField(null=True)
    facebook=models.URLField(null=True)
    
    