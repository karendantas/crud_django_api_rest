# Generated by Django 5.0.3 on 2024-03-08 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0002_user_age_user_email_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_nickname',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False),
        ),
    ]
