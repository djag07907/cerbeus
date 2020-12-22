# Generated by Django 2.2.13 on 2020-12-18 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0007_remove_cliente_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('Natural', 'Natural'), ('Jurídica', 'Jurídica')], default='Natural', max_length=10),
        ),
    ]
