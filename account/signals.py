from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Admin, Question_designer, Student, Guest


@receiver(post_save, sender=CustomUser)
def create_role_instance(sender, instance, created, **kwargs):
    if created:  # Only run when a new user is created
        if instance.role == 'admin':
            Admin.objects.create(admin=instance)
        elif instance.role == 'question_desiner':
            Question_designer.objects.create(designer=instance)
        elif instance.role == 'student':
            Student.objects.create(student=instance)
        elif instance.role == 'guest':
            Guest.objects.create(guest=instance)
