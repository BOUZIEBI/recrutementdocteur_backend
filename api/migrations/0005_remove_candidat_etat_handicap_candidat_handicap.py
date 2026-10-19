import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            'api',
            '0004_alter_structure_options_remove_structure_abreviation_and_more'
        ),
    ]

    operations = [
        migrations.CreateModel(
            name='Handicap',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('libelle', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('cree_le', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modifie_le', models.DateTimeField(auto_now=True)),
                ('is_mode', models.BooleanField(blank=True, default=True, null=True)),
                ('supprime_le', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'handicaps',
                'ordering': ['libelle'],
            },
        ),
        migrations.RemoveField(
            model_name='candidat',
            name='etat_handicap',
        ),
        migrations.AddField(
            model_name='candidat',
            name='handicap',
            field=models.ForeignKey(
                to='api.handicap',
                on_delete=django.db.models.deletion.SET_NULL,
                null=True,
                blank=True,
                related_name='candidats_handicap',
                db_column='handicap_uid',
            ),
        ),
    ]