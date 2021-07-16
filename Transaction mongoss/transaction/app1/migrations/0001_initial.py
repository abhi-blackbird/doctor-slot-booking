# Generated by Django 3.2.4 on 2021-06-29 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app1.user')),
            ],
        ),
    ]