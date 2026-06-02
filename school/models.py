from django.db import models
from django.core.validators import RegexValidator


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, blank=True)
    qualification = models.CharField(max_length=300, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='teachers/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Teachers"

    def __str__(self):
        return f"{self.name} - {self.designation}"


class Headmaster(models.Model):
    name = models.CharField(max_length=200)
    qualification = models.CharField(max_length=300, blank=True)
    took_office = models.DateField(null=True, blank=True)
    left_office = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    image = models.ImageField(upload_to='headmasters/', blank=True, null=True)
    biography = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'took_office']

    def __str__(self):
        return self.name


class Alumni(models.Model):
    name = models.CharField(max_length=200)
    class_year = models.CharField(max_length=50, blank=True, verbose_name="Class Year/Batch")
    notability = models.TextField(blank=True, verbose_name="Notable For")
    image = models.ImageField(upload_to='alumni/', blank=True, null=True)
    reference_link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Notable Alumni"

    def __str__(self):
        return self.name


class AboutInfo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = "About Page Section"
        verbose_name_plural = "About Page Sections"

    def __str__(self):
        return self.title


class SchoolInfo(models.Model):
    name_bn = models.CharField(max_length=300, verbose_name="School Name (Bengali)", default="বিন্দুবাসিনী সরকারি বালক উচ্চ বিদ্যালয়")
    name_en = models.CharField(max_length=300, verbose_name="School Name (English)", default="Bindu Basini Government Boys' High School")
    motto = models.CharField(max_length=300, default="শিক্ষাই আলো — Education is Light")
    established_year = models.CharField(max_length=20, default="1880")
    address = models.TextField(default="Kazi Nazrul Islam Sarani, Nirala Mor, Tangail, Bangladesh")
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    eiin = models.CharField(max_length=20, default="114680")
    logo = models.ImageField(upload_to='school/', blank=True, null=True)
    favicon = models.ImageField(upload_to='school/', blank=True, null=True)
    about_short = models.TextField(blank=True, help_text="Short description for homepage")

    class Meta:
        verbose_name_plural = "School Information"

    def __str__(self):
        return self.name_en


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Subject(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, blank=True, help_text="Font Awesome icon class (e.g. 'fas fa-book')")
    image = models.ImageField(upload_to='clubs/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Clubs"

    def __str__(self):
        return self.name


class SchoolBuilding(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='buildings/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Achievement(models.Model):
    title = models.CharField(max_length=300)
    year = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} ({self.year})" if self.year else self.title


class DeveloperInfo(models.Model):
    name = models.CharField(max_length=200, default="MD ABU SALEHIN")
    title = models.CharField(max_length=300, default="Web Developer & System Architect")
    description = models.TextField(blank=True, help_text="Short bio for the developer page")
    portfolio_url = models.URLField(default="https://mdsalehin.pro.bd/")
    image_url = models.URLField(default="https://mdsalehin.pro.bd/me.jpg")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Developer Info"

    def __str__(self):
        return self.name
