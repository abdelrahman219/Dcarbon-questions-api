# Generated by Django 4.2.7 on 2023-11-12 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0002_remove_useranswer_answer_useranswer_answer_number_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAnswer',
            new_name='Answer',
        ),
        migrations.AddField(
            model_name='question',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
