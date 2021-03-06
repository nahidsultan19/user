# Generated by Django 3.1.4 on 2021-01-16 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20210110_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='album',
            name='genre',
        ),
        migrations.AddField(
            model_name='track',
            name='album_title',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='music.album'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='artist_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='music.artist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='genre',
            field=models.CharField(choices=[('Rock', 'Rock'), ('Metal', 'Metal'), ('Folk', 'Folk'), ('Pop', 'Pop')], default=0, max_length=10),
            preserve_default=False,
        ),
    ]
