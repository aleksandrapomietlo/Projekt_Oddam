

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_token_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='befc6498-3c2e-4f4f-bc77-ffd399cfd692', max_length=64, unique=True),
        ),
    ]