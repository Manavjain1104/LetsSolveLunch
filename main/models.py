from taggit.managers import TaggableManager
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# all models for LetsSolveLunch
class Restaurant(models.Model):
    name            = models.CharField(max_length=50)
    email           = models.EmailField(primary_key= True, max_length=254)
    open_time       = models.TimeField(auto_now_add=False)
    end_time        = models.TimeField(auto_now_add=False)

class Meal(models.Model):
    meal_id                = models.BigAutoField(primary_key = True)
    name                   = models.CharField(max_length=30)
    description            = models.CharField(max_length=200)
    picture                = models.ImageField(null=True, blank = True, upload_to="images/")
    number_of_reservations = models.IntegerField(default=0)
    price_staff            = models.DecimalField(max_digits=5, decimal_places=2)
    price_student          = models.DecimalField(max_digits=5, decimal_places=2)
    restaurant             = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False)
    tags                   = TaggableManager()

class Customer(models.Model):
    COMP = "Computing/JMC"
    MATH = "Math"
    BIOMED = "Bio-medical engineering"
    MEDICINE = "Medicine"

    DEPARTMENTS = [COMP, MATH, BIOMED, MEDICINE]

    DEPT_CHOICES = (
    (COMP, "Computing/JMC"),
    (MATH, "Math"),
    (BIOMED, "Bio-medical engineering"),
    (MEDICINE, "Medicine"),
    )

    name           = models.CharField(max_length=30)
    email          = models.EmailField(primary_key = True)
    is_student     = models.BooleanField(default=True, null=True)
    loyalty_points = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    department     = models.CharField(max_length=30,
                        choices=DEPT_CHOICES,
                        default=COMP)

class Reservation(models.Model):
    order_no    = models.BigAutoField(primary_key = True)
    datetime    = models.DateTimeField(auto_now_add=True)
    meal        = models.ForeignKey(Meal, on_delete=models.CASCADE)
    customer    = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    collected   = models.BooleanField(default=False)
    qr          = models.ImageField(blank = True, upload_to="images/")

    def __str__(self) -> str:
        return str(self.order_no)

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(self.order_no)
        qr_offset = Image.new('RGB', (310,310), 'white')
        qr_offset.paste(qr_image)
        files_name = f'{str(self.order_no)}.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.qr.save(files_name, File(stream),save=False)
        qr_offset.close()
        super().save(*args, **kwargs)