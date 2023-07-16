from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='6fd5558b-4527-4ae0-a43b-b64d3c2b8c91', max_length=64, unique=True),
        ),
    ]