# Generated by Django 2.2.6 on 2019-10-17 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_abandonedsignup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('current_plan', models.CharField(blank=True, choices=[('Free', 'Free'), ('Mini', 'Mini'), ('Biggie', 'Biggie'), ('Maxxie', 'Maxxie')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
