from django.db import models

class AllUsers (models.Model): 
    name = models.CharField(max_length=12)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name