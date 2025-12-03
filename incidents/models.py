from django.db import models
from django.utils import timezone
import uuid

STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Reviewed', 'Reviewed'),
    ('Solved', 'Solved'),
)

class Incident(models.Model):
    # User Information
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=20, blank=True, null=True)

    # Incident Information
    incident_type = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)
    date_lodged = models.DateTimeField(default=timezone.now)

    # Auto-generated reference ID
    reference_id = models.CharField(max_length=20, unique=True, editable=False)

    # Evidence file (optional)
    evidence_file = models.FileField(upload_to='evidence/', blank=True, null=True)

    # Admin Workflow Fields
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    admin_notes = models.TextField(blank=True, null=True)
    admin_report = models.TextField(blank=True, null=True)
    reported_by_admin = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Generate unique reference ID only on creation
        if not self.reference_id:
            self.reference_id = str(uuid.uuid4()).split('-')[0].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_id} - {self.incident_type}"
