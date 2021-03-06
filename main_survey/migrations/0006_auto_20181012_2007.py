# Generated by Django 2.1 on 2018-10-12 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_survey', '0005_auto_20181012_0926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logtable',
            old_name='cinque',
            new_name='l1',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='diciannove',
            new_name='l10',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='diciassette',
            new_name='l11',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='dieci',
            new_name='l12',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='dodici',
            new_name='l13',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='otto',
            new_name='l14',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='due',
            new_name='l15',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='ventitre',
            new_name='l19',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='diciotto',
            new_name='l2',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='idoneo',
            new_name='l20',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='quattordici',
            new_name='l21',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='nove',
            new_name='l22',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='sedici',
            new_name='l23',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='tredici',
            new_name='l24',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='venti',
            new_name='l25',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='quattro',
            new_name='l3',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='quindici',
            new_name='l4',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='tre',
            new_name='l5',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='sei',
            new_name='l6',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='sette',
            new_name='l7',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='venticinque',
            new_name='l8',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='undici',
            new_name='l9',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='lingua',
            new_name='lang',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='ventiquattro',
            new_name='valid',
        ),
        migrations.RenameField(
            model_name='logtable',
            old_name='quando',
            new_name='when',
        ),
        migrations.RemoveField(
            model_name='logtable',
            name='uno',
        ),
        migrations.RemoveField(
            model_name='logtable',
            name='ventidue',
        ),
        migrations.RemoveField(
            model_name='logtable',
            name='ventuno',
        ),
        migrations.AddField(
            model_name='logtable',
            name='l16',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='logtable',
            name='l17',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='logtable',
            name='l18',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
