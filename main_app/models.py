from django.db import models

<<<<<<< HEAD
# Create your models here.

=======
>>>>>>> 8ef656553446a01c279f0b34583b1507b163af7b
class Cat(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
<<<<<<< HEAD
    return self.name
=======
    return self.name
>>>>>>> 8ef656553446a01c279f0b34583b1507b163af7b
