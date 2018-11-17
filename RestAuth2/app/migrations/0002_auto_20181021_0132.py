# Generated by Django 2.1.2 on 2018-10-20 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kingdom', models.IntegerField(default=0)),
                ('name', models.CharField(default='', max_length=32)),
                ('energy', models.IntegerField(default=100)),
            ],
        ),
        migrations.AddField(
            model_name='cx',
            name='owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Unit'),
        ),
        migrations.AddField(
            model_name='gameuser',
            name='units',
            field=models.ManyToManyField(to='app.Unit'),
        ),
    ]