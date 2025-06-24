from django.db import models

class Role(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Region(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Utilisateur(models.Model):
    Utilisateur_id=models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Service(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Profile(models.Model):
    Profile_id=models.AutoField(primary_key=True)
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, db_column='utilisateur_id')
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='photos_profils/', blank=True, null=True)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return f"Profil de {self.utilisateur.nom}"

class Portfolio(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, db_column='Profile_id')
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)

    def __str__(self):
        return self.titre
