

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_token_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='5a089650-67b6-4786-9ae2-c2475d77cfa7', max_length=64, unique=True),
        ),
    ]