# Generated by Django 2.2.2 on 2020-02-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0002_booking_product_profile_send_feedback_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]