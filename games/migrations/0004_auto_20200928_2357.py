# Generated by Django 3.1.1 on 2020-09-28 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20200928_1437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playerscore',
            options={'ordering': ('-score',)},
        ),
        migrations.RenameField(
            model_name='playerscore',
            old_name='score_data',
            new_name='score_date',
        ),
        migrations.AlterField(
            model_name='game',
            name='game_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='games.gamecategory'),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='gamecategory',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]
