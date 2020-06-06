from django.db import models

class Vehicle(models.Model):
  placa_text = models.CharField(max_length=6)
  VEHICLE_TYPE = (
        ('Carro', 'Carro'),
        ('Moto', 'Moto'),
  )
  vehicle_type = models.CharField(max_length=5, choices=VEHICLE_TYPE)
  
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.placa_text