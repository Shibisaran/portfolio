from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(help_text="Proficiency percentage from 0 to 100")

    def __str__(self) -> str:
        return f"{self.name} ({self.level}%)"


class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    image = models.ImageField(upload_to='certifications/', blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.issuing_organization}"


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.email}"
