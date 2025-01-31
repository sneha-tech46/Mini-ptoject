# Generated by Django 3.2.24 on 2024-03-04 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the party', max_length=100, unique=True)),
                ('symbol', models.ImageField(help_text='Email address of the party', upload_to='party_symbols/')),
                ('leader', models.CharField(help_text='Leader of the party', max_length=100)),
                ('foundation_date', models.DateField(help_text='Foundation date of the party')),
                ('email', models.EmailField(blank=True, help_text='Email address of the party', max_length=100, null=True)),
                ('password', models.CharField(blank=True, help_text='Password of the party', max_length=100, null=True)),
                ('status', models.CharField(help_text='Status of the party', max_length=100)),
                ('phone', models.CharField(help_text='Phone number of the party', max_length=100)),
            ],
        ),
    ]
