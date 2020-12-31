# Generated by Django 3.1.4 on 2020-12-31 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('city_name', models.CharField(max_length=50)),
                ('information', models.TextField(blank=True, null=True)),
                ('year', models.PositiveSmallIntegerField()),
                ('month', models.PositiveSmallIntegerField()),
                ('day', models.PositiveSmallIntegerField()),
                ('end_month', models.PositiveSmallIntegerField()),
                ('end_day', models.PositiveSmallIntegerField()),
                ('event_specs', models.CharField(blank=True, max_length=256, null=True)),
                ('wca_delegate', models.TextField(blank=True, null=True)),
                ('organizer', models.TextField(blank=True, null=True)),
                ('venue', models.CharField(max_length=240, null=True)),
                ('venue_address', models.CharField(blank=True, max_length=120, null=True)),
                ('venue_details', models.CharField(blank=True, max_length=120, null=True)),
                ('external_website', models.CharField(blank=True, max_length=200, null=True)),
                ('cell_name', models.CharField(max_length=45)),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longitude', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('record_name', models.CharField(blank=True, max_length=3, null=True)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('zoom', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('iso2', models.CharField(blank=True, max_length=2, null=True)),
                ('continent', models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.continent')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=54)),
                ('rank', models.IntegerField()),
                ('format', models.CharField(max_length=10)),
                ('cell_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('sort_by', models.CharField(max_length=255)),
                ('sort_by_second', models.CharField(max_length=255)),
                ('expected_solve_count', models.IntegerField()),
                ('trim_fastest_n', models.IntegerField()),
                ('trim_slowest_n', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('subid', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True)),
                ('country', models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.country')),
            ],
            options={
                'base_manager_name': 'objects',
                'unique_together': {('id', 'subid')},
            },
        ),
        migrations.CreateModel(
            name='RoundType',
            fields=[
                ('id', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('rank', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('cell_name', models.CharField(max_length=45)),
                ('final', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Scramble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scramble_id', models.PositiveIntegerField()),
                ('group_id', models.CharField(max_length=3)),
                ('is_extra', models.IntegerField()),
                ('scramble_num', models.IntegerField()),
                ('scramble', models.TextField()),
                ('competition', models.ForeignKey(max_length=32, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.competition')),
                ('event', models.ForeignKey(max_length=6, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.event')),
                ('round_type', models.ForeignKey(max_length=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.roundtype')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.SmallIntegerField()),
                ('best', models.IntegerField(db_index=True)),
                ('average', models.IntegerField(db_index=True)),
                ('person_name', models.CharField(blank=True, max_length=80, null=True)),
                ('value1', models.IntegerField()),
                ('value2', models.IntegerField()),
                ('value3', models.IntegerField()),
                ('value4', models.IntegerField()),
                ('value5', models.IntegerField()),
                ('regional_single_record', models.CharField(blank=True, max_length=3, null=True)),
                ('regional_average_record', models.CharField(blank=True, max_length=3, null=True)),
                ('competition', models.ForeignKey(max_length=32, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.competition')),
                ('country', models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.country')),
                ('event', models.ForeignKey(max_length=6, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.event')),
                ('format', models.ForeignKey(max_length=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.format')),
                ('person', models.ForeignKey(max_length=10, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.person')),
                ('round_type', models.ForeignKey(max_length=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.roundtype')),
            ],
        ),
        migrations.CreateModel(
            name='RanksSingle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best', models.IntegerField(null=True)),
                ('world_rank', models.IntegerField()),
                ('continent_rank', models.IntegerField()),
                ('country_rank', models.IntegerField()),
                ('event', models.ForeignKey(max_length=6, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.event')),
                ('person', models.ForeignKey(max_length=10, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.person')),
            ],
        ),
        migrations.CreateModel(
            name='RanksAverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best', models.IntegerField(null=True)),
                ('world_rank', models.IntegerField()),
                ('continent_rank', models.IntegerField()),
                ('country_rank', models.IntegerField()),
                ('event', models.ForeignKey(max_length=6, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.event')),
                ('person', models.ForeignKey(max_length=10, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.person')),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='country',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.country'),
        ),
        migrations.AddField(
            model_name='competition',
            name='delegates',
            field=models.ManyToManyField(related_name='delegated_comps', to='wca.Person'),
        ),
        migrations.AddField(
            model_name='competition',
            name='events',
            field=models.ManyToManyField(to='wca.Event'),
        ),
        migrations.AddField(
            model_name='competition',
            name='organizers',
            field=models.ManyToManyField(related_name='organized_comps', to='wca.Person'),
        ),
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('championship_type', models.CharField(max_length=191)),
                ('competition', models.ForeignKey(max_length=191, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wca.competition')),
            ],
        ),
    ]
