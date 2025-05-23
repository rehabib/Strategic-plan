# Generated by Django 5.2 on 2025-04-27 05:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_astrategicgoal_directorplan_dstrategicgoal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='directorplan',
            old_name='Budget_Government',
            new_name='april',
        ),
        migrations.RenameField(
            model_name='directorplan',
            old_name='Budget_Society',
            new_name='auguest',
        ),
        migrations.RenameField(
            model_name='directorplan',
            old_name='Other_Budget',
            new_name='budget',
        ),
        migrations.RenameField(
            model_name='directorplan',
            old_name='aim',
            new_name='budget_year_aim',
        ),
        migrations.RenameField(
            model_name='directorplan',
            old_name='base_value',
            new_name='december',
        ),
        migrations.RemoveField(
            model_name='agencyplan',
            name='astrategic_goal',
        ),
        migrations.RemoveField(
            model_name='directorplan',
            name='Beneficial_Body',
        ),
        migrations.RemoveField(
            model_name='directorplan',
            name='Beneficial_Society',
        ),
        migrations.RemoveField(
            model_name='directorplan',
            name='Created_at',
        ),
        migrations.RemoveField(
            model_name='directorplan',
            name='main_activity',
        ),
        migrations.RemoveField(
            model_name='directorplan',
            name='year',
        ),
        migrations.AddField(
            model_name='agencyplan',
            name='strategic_goal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.astrategicgoal'),
        ),
        migrations.AddField(
            model_name='directorplan',
            name='acountable_person',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='directorplan',
            name='expected_result',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='directorplan',
            name='february',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='directorplan',
            name='january',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='directorplan',
            name='july',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='directorplan',
            name='june',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='directorplan',
            name='march',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='directorplan',
            name='may',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='directorplan',
            name='november',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='directorplan',
            name='october',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='directorplan',
            name='september',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agencyplan',
            name='measurement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.measurement'),
        ),
        migrations.AlterField(
            model_name='agencyplan',
            name='perspective',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.perspective'),
        ),
        migrations.AlterField(
            model_name='directorplan',
            name='measurement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.measurement'),
        ),
        migrations.AlterField(
            model_name='directorplan',
            name='perspective',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.perspective'),
        ),
        migrations.AddField(
            model_name='directorplan',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.activity'),
        ),
    ]
