# Generated by Django 5.1.2 on 2024-10-31 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_drink_drinks_drink_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrinksCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='drinks',
            old_name='drink_name',
            new_name='drink',
        ),
        migrations.AddField(
            model_name='drinks',
            name='category_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='mainapp.drinkscategory'),
        ),
    ]
