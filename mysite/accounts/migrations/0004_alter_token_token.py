
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_token_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='a138f17a-0d2a-42dd-a3c5-b241a8db661c', max_length=64, unique=True),
        ),
    ]