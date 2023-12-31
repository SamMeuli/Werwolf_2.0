# Generated by Django 3.2.20 on 2023-08-09 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_key', models.PositiveIntegerField(default=1)),
                ('player_number', models.PositiveIntegerField(default=8)),
                ('werwolf_number', models.PositiveIntegerField(default=2)),
                ('include_amor', models.BooleanField(default=False)),
                ('include_blinzel', models.BooleanField(default=False)),
                ('include_seher', models.BooleanField(default=False)),
                ('include_hexe', models.BooleanField(default=False)),
                ('game_host', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('is_evil', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(default='Guest', max_length=20)),
                ('is_alive', models.BooleanField()),
                ('joined_games', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.game')),
                ('player_key', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('roletype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.role')),
            ],
        ),
    ]
