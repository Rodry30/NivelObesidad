from cProfile import label
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class FormPrediccion(models.Model):
                    GENERO_CHOICES = [
                        (1, "Masculino"),
                        (2, "Femenino"),
                    ]

                    FAVC_CHOICES = [
                        (1, "Sí"),
                        (0, "No"),
                    ]

                    FCVC_CHOICES = [
                        (1, "Nunca"),
                        (2, "A veces"),
                        (3, "Siempre"),
                    ]

                    NCP_CHOICES = [
                        (1, "De una a dos"),
                        (2, "Tres"),
                        (3, "Más de tres"),
                    ]

                    CAEC_CHOICES = [
                        (1, "De una a dos"),
                        (2, "Tres"),
                        (3, "Más de tres"),
                    ]

                    CH20_CHOICES = [
                        (1, "Menor a 1L"),
                        (2, "Entre 1L y 2L"),
                        (3, "Mayor a 2L"),
                    ]

                    SCC_CHOICES = [
                        (0, "Sí"),
                        (1, "No"),
                    ]

                    FAF_CHOICES = [
                        (0, "No"),
                        (1, "1-2 días"),
                        (2, "2-4 días"),
                        (3, "4-5 días"),
                    ]

                    TUE_CHOICES = [
                        (0, "0 a 2h"),
                        (1, "3h a 5h"),
                        (2, "Más de 5h"),
                    ]

                    CALC_CHOICES = [
                        (0, "No"),
                        (1, "A veces"),
                        (2, "Frecuentemente"),
                        (3, "Siempre"),
                    ]

                    MTRANS_CHOICES = [
                        (0, "Caminar"),
                        (1, "Bicicleta"),
                        (2, "Motocicleta"),
                        (3, "Transporte público"),
                        (4, "Automóvil"),
                    ]

                    genero = models.IntegerField( choices=GENERO_CHOICES)
                    edad = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])
                    estatura = models.FloatField( validators=[MinValueValidator(0.5), MaxValueValidator(2.5)])  
                    peso = models.FloatField( validators=[MinValueValidator(20), MaxValueValidator(300)])  
                    afdeo = models.IntegerField(choices=[(0, "No"), (1, "Sí")])
                    favc = models.IntegerField(choices=FAVC_CHOICES)
                    fcvc = models.IntegerField(choices=FCVC_CHOICES)
                    ncp = models.IntegerField(choices=NCP_CHOICES)
                    caec = models.IntegerField(choices=CAEC_CHOICES)
                    tabaco = models.IntegerField(choices=[(0, "No"), (1, "Sí")])
                    ch20 = models.IntegerField(choices=CH20_CHOICES)
                    scc = models.IntegerField(choices=SCC_CHOICES)
                    faf = models.IntegerField(choices=FAF_CHOICES)
                    tue = models.IntegerField(choices=TUE_CHOICES)
                    calc = models.IntegerField(choices=CALC_CHOICES)
                    mtrans = models.IntegerField(choices=MTRANS_CHOICES)


