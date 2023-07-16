from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=16)),
                ('city', models.CharField(max_length=16)),
                ('zip_code', models.CharField(max_length=6)),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.TimeField()),
                ('pick_up_comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=128)),
                ('type', models.CharField(choices=[(1, 'Fundacja'), (2, 'Organizacja pozarzadowa'), (3, 'Zbiorka lokalna')], default=1, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.institution')),
            ],
        ),
        migrations.AddField(
            model_name='institution',
            name='categories',
            field=models.ManyToManyField(null=True, through='main.InstitutionCategory', to='main.Category'),
        ),
        migrations.CreateModel(
            name='DonationCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('donation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.donation')),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='categories',
            field=models.ManyToManyField(null=True, through='main.DonationCategory', to='main.Category'),
        ),
        migrations.AddField(
            model_name='donation',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.institution'),
        ),
        migrations.AddField(
            model_name='donation',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]