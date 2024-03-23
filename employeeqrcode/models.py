from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
from django.urls import reverse

class Employee(models.Model):
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    date_joined = models.DateField()
    email = models.EmailField()
    qr_code = models.ImageField(upload_to='employee_qrcodes', blank=True)

    def get_absolute_url(self):
        return reverse('employee_profile', kwargs={'pk': self.pk})
    
    def __str__(self):
        return f"Employee {self.name} works as {self.role}"
        
    def save(self, *args, **kwargs):
        if not self.qr_code: 
            if not self.pk:
                super().save(*args, **kwargs)
            employee_id = self.pk
            profile_url = reverse('employee_profile', args=[employee_id])
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(profile_url)
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="black", back_color="white")

            # Save QR code image to ImageField
            temp_buffer = BytesIO()
            qr_img.save(temp_buffer, format="PNG")
            temp_buffer.seek(0)
            self.qr_code.save(f"{self.name}_qr.png", File(temp_buffer))

        super().save(*args, **kwargs)