from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "api",
            "0006_remove_historique_etat_handicap_historique_handicap",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidat",
            name="handicap",
            field=models.ForeignKey(
                to="api.handicap",
                on_delete=django.db.models.deletion.SET_NULL,
                null=True,
                blank=True,
                related_name="candidats_handicap",
                db_column="handicap_uid",
            ),
        ),
    ]