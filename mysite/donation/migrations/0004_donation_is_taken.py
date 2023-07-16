
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0003_alter_institution_name_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
    ]