from pyexpat import model
from django.core import validators
from django.core.checks import messages
from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.deletion import CASCADE

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt =  models.CharField(max_length=100)
    image = models.ImageField(upload_to = "posts", null=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(null = True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,on_delete=models.SET_NULL, null = True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    user_name =  models.CharField(max_length=120)
    user_mail = models.EmailField()
    text = models.TextField(max_length=300)
    posts = models.ForeignKey(Post,on_delete=CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.user_name} {self.text}"
    