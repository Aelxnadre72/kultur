# Generated by Django 3.2.12 on 2022-02-24 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stili', '0008_event_eventarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stili.user'),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventDifficulty',
            field=models.CharField(choices=[('1', 'Lett'), ('2', 'Middels'), ('3', 'Vankselig')], max_length=1),
        ),
    ]
