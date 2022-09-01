from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()


    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=50)
    description = models.TextField()


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category



class Article(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    body = models.TextField()
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['-create_date']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f"/article/{self.slug}"