
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0004_donation_is_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='status_change_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]