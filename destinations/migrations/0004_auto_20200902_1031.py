# Generated by Django 2.0.7 on 2020-09-02 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0003_remove_destination_pretty_picture1'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='pretty_picture2',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='pretty_picture3',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]
