from django.db import migrations

def seed_data(apps, schema_editor):
    Category = apps.get_model('myapp','Category')
    Tag = apps.get_model('myapp','Tag')
    Post = apps.get_model('myapp','Post')

    cat_news = Category.objects.create(name='Новости')
    cat_tutorial = Category.objects.create(name='Обучение')

    t_django = Tag.objects.create(name='Django')
    t_python = Tag.objects.create(name='Python')
    t_web = Tag.objects.create(name='Web')

    p1 = Post.objects.create(title='Первый пост', content='Содержимое первого поста', category=cat_news)
    p1.tags.add(t_python, t_web)

    p2 = Post.objects.create(title='Гайд по Django', content='Мини-гайд', category=cat_tutorial)
    p2.tags.add(t_django, t_python)

def unseed_data(apps, schema_editor):
    Category = apps.get_model('myapp','Category')
    Tag = apps.get_model('myapp','Tag')
    Post = apps.get_model('myapp','Post')
    Post.objects.all().delete()
    Tag.objects.all().delete()
    Category.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('myapp','0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_code=unseed_data)
    ]
