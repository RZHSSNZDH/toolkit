from django.db import models

class link(models.Model):
    main = models.CharField(max_length=200)
    short = models.CharField(max_length=4)

    def __str__(self):
        return self.main
