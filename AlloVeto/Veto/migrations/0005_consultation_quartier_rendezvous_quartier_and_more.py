# Generated by Django 4.1.6 on 2023-08-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veto', '0004_alter_partner_site_alter_team_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='quartier',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='quartier',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='Motif',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consultation',
            name='Vacc',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='couleur',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='nomAnimal',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='race',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='sexe',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='Message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='heure',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='status',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]