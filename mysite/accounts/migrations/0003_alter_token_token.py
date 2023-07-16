
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_token_active_alter_token_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='fd62596b-0abc-4a6b-b525-ef6222aa1f23', max_length=64, unique=True),
        ),
    ]