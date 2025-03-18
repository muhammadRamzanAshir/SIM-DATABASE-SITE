from django.db import models

ICON_CHOICES = [
    ("flaticon-green",    "Green Icon"),
    ("flaticon-rocket",   "Rocket Icon"),
    ("flaticon-settings", "Settings Icon"),
    ("flaticon-global",   "Global Icon"),
    ("flaticon-shield",   "Shield Icon"),
    ("flaticon-server",   "Server Icon"),
    ("flaticon-cloud",    "Cloud Icon"),
    ("flaticon-security", "Security Icon"),
    ("flaticon-database", "Database Icon"),
]

class NavbarItem(models.Model):
    name        = models.CharField(max_length=100)
    url         = models.CharField(max_length=255,blank=True, null=True)
    is_active   = models.BooleanField(default=True)
    parent      = models.ForeignKey(
        "self",
        on_delete       = models.CASCADE,
        blank           = True,
        null            = True,
        related_name    = "submenus"
    )

    def __str__(self):
        return self.name

    def is_submenu(self):
        return self.parrent is not None

class Slider(models.Model):
    title       = models.CharField(max_length=255)
    description  =  models.TextField(blank=True, null=True) 
    button_text = models.CharField(max_length=50, default="Get Started")
    button_link = models.URLField(default="#")
    image       = models.ImageField(upload_to="slider_images/")

    def __str__(self):
        return self.title

class Service(models.Model):
    title               =   models.CharField(max_length=255)
    description         =   models.TextField()
    icon_class          =   models.CharField(max_length=50, choices=ICON_CHOICES, default="flaticon-green")
    link                =   models.URLField(default="http://localhost")
    order_number        =   models.IntegerField(default=1)
    service_heading     =   models.CharField(max_length=50 , default="Default Heading")
    service_subheading  =   models.CharField(max_length=50 , default="Default subHeading")

    def __str__(self):
        return self.title

class SectionTitle(models.Model):
    title       =   models.CharField(max_length=255, default="Dummy Text")
    subtitle    =   models.CharField(max_length=255, default="Dummy Text")

    def __str__(self):
        return self.title

class  Partner(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="partners/")

    def __str__(self):
        return self.name

class AboutUs(models.Model):
    title           = models.CharField(max_length=255, default="Dummy Text")
    subtitle        = models.CharField(max_length=255, default="DUmmy Text")
    description_1   = models.TextField(default="Default Descripton 1")
    description_2   = models.TextField(default="Default Description 2")
    button_text     = models.CharField(max_length=50, default="Get started")
    button_link     = models.URLField(max_length=100, default="#")
    image           = models.ImageField(upload_to="about_images/", default="default.jpg")
    
    def __str__(self):
        return self.title


class PricingPlan(models.Model):
    PLAN_CHOICES = (
        ("monthly", "Monthly"),
        ("yearly", "Yearly"),
    )
    
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    plan_type = models.CharField(max_length=10, choices=PLAN_CHOICES)  # Monthly or Yearly
    features = models.TextField(help_text="Enter features separated by a comma")
    image = models.ImageField(upload_to="pricing_images/", blank=True, null=True)

    def get_features_list(self):
        return self.features.split(",")

    def __str__(self):
        return f"{self.title} - {self.plan_type}"

class SupportInfo(models.Model):
    title        =   models.CharField(max_length=255, default="dummy text")
    subtitle     =   models.CharField(max_length=255, default="dummy text")
    description  =   models.TextField(default="our expert")
    phone_number =   models.CharField(max_length=20, default="xx-xxxxxx")
    text_field   =   models.TextField(max_length=50, default="text_us")

    def __str__(self):
        return self.title


class PhoneDetail(models.Model):
    number = models.CharField(max_length=20, primary_key=True)  # Ensure this is the primary key
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    cnic = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set timestamp

    def __str__(self):
        return self.number  # Display phone number in admin panel
    

class Footer(models.Model):
    logo = models.ImageField(upload_to='footer_logos/', default='default_logo.png')
    phone = models.CharField(max_length=20, default='+1 514 648 256')
    email = models.EmailField(default='youremail@gmail.com')
    address = models.TextField(default='123 East 26th Street, Fifth Floor, New York, NY 10011')
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Footer Settings"
