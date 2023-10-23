from django.db import migrations, models

from dramatiq_pg.schema import generate_init_sql

class Migration(migrations.Migration):
    initial = True

    operations = [
        migrations.CreateModel(
            name="PgDramatiqTask",
            fields=[
                ("message_id", models.UUIDField(primary_key=True, serialize=False)),
                ("queue_name", models.TextField(default="default")),
                (
                    "state",
                    models.TextField(
                        choices=[
                            ('queued', 'Queued'),
                            ('consumed', 'Consumed'),
                            ('rejected', 'Rejected'),
                            ('done', 'Done'),
                        ],
                        default="queued",
                    ),
                ),
                ("mtime", models.DateTimeField()),
                ("message", models.JSONField()),
                ("result", models.JSONField()),
                ("result_ttl", models.DateTimeField()),
            ],
            options={"db_table": "dramatiq_queue", "managed": False},
        ),
        migrations.RunSQL(generate_init_sql(schema="public", prefix="dramatiq_")),
    ]
