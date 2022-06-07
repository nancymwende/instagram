# Generated by Django 4.0.5 on 2022-06-07 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_photo', models.ImageField(blank=True, upload_to='images/')),
                ('bio', models.TextField(blank=True, max_length=100)),
                ('name', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('image_name', models.CharField(max_length=50)),
                ('image_caption', models.TextField(max_length=100)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('likes', models.ManyToManyField(blank=True, default=None, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insta.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=250)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='insta.image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
