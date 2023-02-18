# Generated by Django 4.1.5 on 2023-02-18 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainApp', '0004_lang_alter_comment_snippet_alter_snippet_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='snippet',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL),
        ),
    ]
