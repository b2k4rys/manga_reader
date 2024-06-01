from django.db import models

# Create your models here.

class Categories(models.Model):
  name = models.CharField(max_length=150, verbose_name='Name')
  slug = models.SlugField(max_length=200, blank=True, null=True, verbose_name='URL')

  class Meta:
    db_table = 'category'
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

  def __str__(self) -> str:
    return self.name

class Types(models.Model):
  type = models.CharField(max_length=150)

  def __str__(self) -> str:
    return self.type

  
class Manga(models.Model):
  name = models.CharField(max_length=150, unique=True, verbose_name='Name')
  name_in_jap = models.CharField(max_length=150, unique=True, verbose_name='Name_in_jap')

  categories = models.ManyToManyField(Types)

  description = models.TextField(blank=True, null=True, verbose_name='Desciption')
  category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Type')
  status = models.CharField(max_length=150, verbose_name='Status')
  author = models.TextField(blank=True, null=True, verbose_name='Author')
  magazine = models.TextField(blank=True, null=True, verbose_name='Magazine')
  published = models.TextField(blank=True, null=True, verbose_name='Publish_Date')
  score = models.DecimalField(default=0.00, max_digits=4 ,decimal_places=2)
  views = models.DecimalField(default=0.00, max_digits=100, decimal_places=0)
  image = models.ImageField(upload_to='manga_images', blank=True,  null=True)
  slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

  number_of_chapters = models.DecimalField(default=0.00, max_digits=5 ,decimal_places=0, verbose_name="Number of Chapters")

  class Meta:
    db_table = 'Manga'
    verbose_name = 'Manga'
    verbose_name_plural = 'Mangas'

  def __str__(self) -> str:
    return self.name
  
