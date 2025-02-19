# Generated by Django 4.2.1 on 2024-11-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-created_at'], name='neapp_post_created_0318ad_idx'),
        ),
    ]
