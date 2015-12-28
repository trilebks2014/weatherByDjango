from django.db import models
from weather.reviews.models import Review
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
from weather.service.models import ServiceSMS
class Profile(models.Model):
    user = models.OneToOneField(User)
    city = models.CharField(max_length=50)
    selectService = models.ForeignKey(ServiceSMS,default=0, on_delete=models.CASCADE)
    def get_reviews(self):
        user_reviews = []
        author_reviews = Review.objects.filter(author=self.user)
        co_author_reviews = Review.objects.filter(co_authors=self.user)
        for r in author_reviews: user_reviews.append(r)
        for r in co_author_reviews: user_reviews.append(r)
        user_reviews.sort(key=lambda r: r.last_update, reverse=True)
        return user_reviews
    def __str__(self):
        return str(self.user)
