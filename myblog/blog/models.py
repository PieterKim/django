from django.db import models

# Create your models here.

# 게시글
class Post(models.Model):
    # FK(Foreign Key)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', blank=True)
    
    title = models.CharField('TITLE', max_length=50)
    description = models.CharField('DESCRIPTION', max_length=100, 
                                   blank=True, 
                                   help_text='simple one-line text.')
    image = models.ImageField('IMAGE', upload_to='blog/%Y/%m/',
                              blank=True, null= True)
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField("CREATE DT", auto_now_add=True)
    update_date = models.DateTimeField("UPDATE DT", auto_now=True)
    like = models.PositiveIntegerField('LIKE', default=0)

    def __str__(self):
        return self.title

## 게시글의 종류를 지정
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField('DESCRIPTION', max_length=100,
                                   blank=True,
                                   help_text='simple one-line text.')

    def __str__(self):
        return self.name


## 게시글의 해시 태그
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

## 댓글
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_date = models.DateTimeField('UPDATE DT', auto_now=True)

    @property
    def short_content(self):
        return self.content[:10]
    
    def __str__(self):
        return self.short_content