
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('type', models.IntegerField(choices=[(0, 'fundacja'), (1, 'organizacja pozarządowa'), (2, 'zbiórka lokalna')], default=0)),
                ('categories', models.ManyToManyField(to='donation.category')),
            ],
        ),
    ]