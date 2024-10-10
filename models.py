from djongo import models

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    admin = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='admin_assignments')
    status = models.CharField(max_length=10, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

