from django.db import models

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    # organizer_email = models.EmailField()
    # date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    # image = models.ImageField(upload_to='images')
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # participants = models.ManyToManyField(Participant, blank=True, null=True)
