# Generated by Django 3.2.9 on 2021-12-12 11:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='作成日'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='image',
            field=models.ImageField(default='profile/default.png', upload_to='images', verbose_name='プロフィール画像'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日'),
        ),
    ]