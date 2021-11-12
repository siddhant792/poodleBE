# Generated by Django 3.2.6 on 2021-11-05 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Title of the document', max_length=50, unique=True)),
                ('subject', models.CharField(help_text='Subject to which the document is related', max_length=50)),
                ('course', models.BooleanField(default=False, help_text='Course to which the document is related')),
                ('semester', models.CharField(help_text='Semester to which the document is related', max_length=50)),
                ('university', models.CharField(help_text='University to which the document is related', max_length=50)),
                ('path', models.CharField(help_text='Path where the document is stored in cloud storage', max_length=200)),
                ('author', models.ForeignKey(help_text='User info who is author of this document', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]