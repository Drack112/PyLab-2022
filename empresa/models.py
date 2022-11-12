from django.db import models

# Create your models here


class Tecnologias(models.Model):
    tecnologia = models.CharField(max_length=50)

    def __str__(self):
        return self.tecnologia


class Empresa(models.Model):
    choices_nicho_mercado = (
        ("M", "Marketing"),
        ("N", "Nutrição"),
        ("D", "Design"),
    )

    logo = models.ImageField(upload_to="logo_empresa")
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    tecnologias = models.ManyToManyField(Tecnologias)
    endereco = models.CharField(max_length=60)
    nicho_mercado = models.CharField(
        max_length=3, choices=choices_nicho_mercado
    )
    caracteristica_empresa = models.TextField()

    def __str__(self):
        return self.nome


class Vagas(models.Model):
    choices_experiencia = (("J", "Júnior"), ("P", "Pleno"), ("S", "Sênior"))

    choices_status = (
        ("I", "Interesse"),
        ("C", "Currículo enviado"),
        ("E", "Entrevista"),
        ("D", "Desafio técnico"),
        ("F", "Finalizado"),
    )

    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=30)
    nivel_experiencia = models.CharField(
        max_length=2, choices=choices_experiencia
    )
    data_final = models.DateField()
    status = models.CharField(max_length=30, choices=choices_status)
    tecnologias_dominadas = models.ManyToManyField(Tecnologias)
    tecnologias_estudar = models.ManyToManyField(
        Tecnologias, related_name="estudar"
    )

    def __str__(self):
        return self.titulo
