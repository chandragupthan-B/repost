# Generated by Django 3.2.2 on 2021-05-31 08:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0013_auto_20210530_0543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='rating',
        ),
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='feed.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
