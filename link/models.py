from django.db import models

class link(models.Model):
    main_link = models.CharField(max_length=200)
