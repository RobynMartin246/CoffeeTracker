from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.utils import timezone

STARS = ((1,'★'),(2,'★★'),(3,'★★★'),(4,'★★★★'),(5,'★★★★★'))
ROAST_CHOICES=((1,'Light'),(2,'Medium'),(3,'Dark'),(4,'Unknown'))
METHOD_CHOICES=((1,'Pour Over'),(2,'AiroPress'),(3,'French Press'),(4,'Drip'),(5,"Unknown"))
ORIGIN=(
	(None, 'Country of Origin'),
    ('Africa', (
            ('kenya', 'Kenya'),
            ('ethiopia', 'Ethiopia'),
            ('burundi', 'Burundi'),
            ('rowanda', 'Rowanda'),
            ('other_africa','Other Africa')
        )
    ),
    ('Central America', (
            ('costa_rica', 'Costa Rica'),
            ('el_salvado', 'El Salvador'),
            ('guatemala', 'Guatemala'),
            ('honduras', 'Honduras'),
            ('panama', 'Panama'),
            ('mexico', 'Mexico'),
            ('nicaragua', 'Nicaragua'),
        )
    ),
    ('South America',(
        ('brazil', 'Brazil'),
        ('bolivia', 'Bolivia'),
        ('colombia','Colombia'),

        )
    ),
    ('Far East',(
        ('bali','Bali'),
        ('papua_new-guinea', 'Papua New Guinea'),
        ('sumatra', 'Sumatra'),
        ('thailand', 'Thailand'),
        ('java', 'Java'),
        ('myanmar', 'Mayanmar'),
        ('vietnam', 'Vietnam'),
        )
    ),
)

class Roast(models.Model):
    origin = models.CharField(max_length=50, null=True, blank=True, choices=ORIGIN)
    roast_name = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    batch_size = models.CharField(max_length=20, null=True, blank=True)
    roast_time = models.CharField(max_length=20, null=True, blank=True)
    roast_levels = models.IntegerField(choices=ROAST_CHOICES, default=1)
    first_crack_start = models.CharField(max_length=20, null=True, blank=True)
    first_crack_end = models.CharField(max_length=20,null=True, blank=True)
    second_crack_start = models.CharField(max_length=20, null=True, blank=True)
    notes = models.TextField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.roast_name

class Acidity(models.Model):
    acidity = models.CharField(max_length=200)
    def __str__(self):
        return self.acidity

class Flavor(models.Model):
    flavor = models.CharField(max_length=200)
    def __str__(self):
        return self.flavor

class Brew(models.Model):
    coffee_name = models.CharField(max_length=200)
    roastery = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    roast_levels = models.IntegerField(choices=ROAST_CHOICES, default=1)
    methods = models.IntegerField(choices=METHOD_CHOICES, default=1)
    acidity = models.ManyToManyField(Acidity, blank=True)
    flavor = models.ManyToManyField(Flavor, blank=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    home_roast = models.ForeignKey('Roast', blank=True, null=True, on_delete=models.CASCADE)
    stars = models.IntegerField(default=1, choices=STARS)
    def __str__(self):
        return self.coffee_name

    def publish(self):
        self.pub_date = timezone.now()
        self.save()



# Create your models here.((1,'Fruity'),(2,'Sweet'),(3,'Nutty'),(4,'Woody'),(5,'Malty'),(6,'Vanilla'),(7,'Caramel')(8,'Chocolate'),(9,'Bitter'),(10,'Clove'))
