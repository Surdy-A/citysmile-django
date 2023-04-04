from distutils.command.upload import upload
import email
from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.text import slugify
import datetime
from django.utils import timezone

Status = (
('For Rent', 'For Rent'),
('For Sale', 'For Sale'),
)

Features = (
('Modern Lawn', 'Modern Lawn'),
('Modern Kitchen', 'Modern Kitchen'),
('Modern Balcony', 'Modern Balcony'),
('Gym Room', 'Gym Room'),
('Servents Room', 'Servents Room'),
('Fire Alarm Available', 'Fire Alarm Available'),
('Swimming Pool', 'Swimming Pool'),
('Modern Laundry', 'Modern Laundry'),
('Pets Box', 'Pets Box'),
('4 Cars Space', '4 Cars Space'),
('New drawing Room', 'New drawing Room'),
('Games Room', 'Games Room'),
('Elevator', 'Elevator'),
('Beautiful Gardens', 'Beautiful Gardens'),
('Basketball court', 'Basketball court'),
)

State = (
('FC' , 'Abuja'),
('AB' , 'Abia'),
('AD' , 'Adamawa'),
('AK' , 'Akwa Ibom'),
('AN' , 'Anambra'),
('BA' , 'Bauchi'),
('BY' , 'Bayelsa'),
('BE' , 'Benue'),
('BO' , 'Borno'),
('CR' , 'Cross River'),
('DE' , 'Delta'),
('EB' , 'Ebonyi'),
('ED' , 'Edo'),
('EK' , 'Ekiti'),
('EN' , 'Enugu'),
('GO' , 'Gombe'),
('IM' , 'Imo'),
('JI' , 'Jigawa'),
('KD' , 'Kaduna'),
('KN' , 'Kano'),
('KT' , 'Katsina'),
('KE' , 'Kebbi'),
('KO' , 'Kogi'),
('KW' , 'Kwara'),
('LA' , 'Lagos'),
('NA' , 'Nassarawa'),
('NI' , 'Niger'),
('OG' , 'Ogun'),
('ON' , 'Ondo'),
('OS' , 'Osun'),
('OY' , 'Oyo'),
('PL' , 'Plateau'),
('RI' , 'Rivers'),
('SO' , 'Sokoto'),
('TA' , 'Taraba'),
('YO' , 'Yobe'),
('ZA' , 'Zamfara'),
)

class Features(models.Model):
    feature_name = models.CharField(max_length=250, choices=Features)

    def __str__(self):
        return self.feature_name


class Property(models.Model):
    city = models.CharField(max_length=250, choices=State)
    address = models.TextField(blank=True, default='')
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    washroom = models.IntegerField()
    carSpace = models.IntegerField()
    roomArea = models.IntegerField(blank=True, default='')
    price = models.FloatField()
    availability = models.BooleanField()
    status = models.CharField(max_length=250, choices=Status, default='')
    description = models.IntegerField()
    agent = models.CharField(max_length=200, blank=True)
    features = models.ManyToManyField(to=Features, default='')
    video = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    createdDate = models.DateTimeField(default=timezone.now)
    updatedDate = models.DateTimeField(default=timezone.now)
    propertyType = models.CharField(max_length=250)
    state =  models.CharField(max_length=250, choices=State)
    postalCode = models.CharField(max_length=250)
    propertyName = models.CharField(max_length=250)
    otherImages = models.FileField(default='')
    image = models.ImageField(upload_to="img")
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(549, 376)],
                                     format='JPEG',
                                     options={'quality': 95})
    slug = models.SlugField(max_length=200, db_index=True, default='')

    def __str__(self):
        return self.propertyName

    def save(self, *args, **kwargs):
        value = self.propertyName
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('property:property_detail', args={self.slug})

