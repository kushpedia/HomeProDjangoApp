# Generated by Django 5.1.1 on 2024-10-28 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profiles_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/profile_pics/'),
        ),
    ]
