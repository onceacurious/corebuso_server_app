from django.db import models
import datetime


class TestUser(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50, default="staff")
    registered_at = models.DateTimeField(auto_now_add=True)

    @property
    def username(self):
        full_name = self.name.split()
        first_name = full_name[0]
        return '%s_%s' % (first_name, self.designation)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-registered_at']
        verbose_name_plural = 'Test Users'


class Inquiry(models.Model):

    INQUIRY_STATUS_CHOICES = [
        ('P', 'Pending'),
        ('R', 'Reviewed'),
        ('D', 'Done'),
    ]

    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField("client's complete name",
                            max_length=100, null=True, blank=True)
    contact = models.CharField(
        max_length=20, null=True, blank=True, default=None)
    company = models.CharField(
        max_length=50, null=True, blank=True, default=None)

    inquiry_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=1, choices=INQUIRY_STATUS_CHOICES, default='P')
    updated_at = models.DateTimeField(auto_now=True)

    # staff = models.ForeignKey(TestUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '%s:(%s)' % (self.name, self.status)

    class Meta:
        ordering = ["-inquiry_at"]
        verbose_name_plural = "inquiries"
