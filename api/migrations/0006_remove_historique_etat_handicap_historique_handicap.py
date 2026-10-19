import django.db.models.deletion

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "api",
            "0005_remove_candidat_etat_handicap_candidat_handicap",
        ),
    ]

    operations = [
    
        migrations.AddField(
            model_name="historique",
            name="handicap",
            field=models.ForeignKey(
                to="api.handicap",
                on_delete=django.db.models.deletion.SET_NULL,
                null=True,
                blank=True,
                related_name="historiques_handicap",
                db_column="handicap_uid",
            ),
        ),
    ]