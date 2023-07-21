from django.db import models
# Create your models here.


class ProfileInfo(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=200)
    overview = models.TextField()
    profilepicture = models.ImageField(upload_to='profilepicture')
    experience = models.PositiveIntegerField()
    project = models.PositiveIntegerField()
    facebook_url = models.URLField(max_length=300)
    github_url = models.URLField(max_length=300)
    cv = models.FileField()

    def __str__(self):
        return self.first_name

class Type(models.Model):
    type = models.CharField(max_length=100, default='Web Development', null=True, unique=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.type

class Services(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    percentage = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    slug = models.SlugField(null=False, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    url = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='portfolio')
    title = models.CharField(max_length=150, default='None', blank=False, null=False)
    description1 = models.TextField()
    description2 = models.TextField(default=None)
    technology_use = models.CharField(max_length=150)
    created_at = models.DateField()
    image1 = models.ImageField(upload_to='portfolio/detail')
    image2 = models.ImageField(upload_to='portfolio/detail')
    image3 = models.ImageField(upload_to='portfolio/detail')
    conclusion1 = models.TextField()
    conclusion2 = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    course = models.CharField(max_length=300)
    school = models.CharField(max_length=400)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)

    def __str__(self):
        return self.school

class Experience(models.Model):
    designation = models.CharField(max_length=300)
    company = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.company

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog')
    description1 = models.TextField()
    quote = models.CharField(max_length=300)
    listing = models.TextField( blank=True, null=True)
    description2 = models.TextField()
    
    def listing_overivew(self):
        return filter(None, (line.strip() for line in self.listing.splitlines()))


    def __str__(self):
        return self.title

class Message(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.username


