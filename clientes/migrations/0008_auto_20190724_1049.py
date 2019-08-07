# Generated by Django 2.2.3 on 2019-07-24 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_auto_20190722_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_doc', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='Documento',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Documento'),
        ),
    ]
