# Generated by Django 4.0 on 2021-12-23 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_client_clientname_user_cellphone_user_clientid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('modelNumber', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('productName', models.CharField(max_length=50, null=True)),
                ('cellTechnology', models.CharField(max_length=50, null=True)),
                ('cellManufacturer', models.CharField(max_length=50, null=True)),
                ('numberofCells', models.IntegerField(null=True, verbose_name=int)),
                ('numberofCellsinSeries', models.IntegerField(null=True, verbose_name=int)),
                ('numberofSeriesStrings', models.IntegerField(null=True, verbose_name=int)),
                ('numberofDiode', models.IntegerField(null=True, verbose_name=int)),
                ('productLength', models.FloatField(null=True, verbose_name=float)),
                ('productWidth', models.FloatField(null=True, verbose_name=float)),
                ('productWeight', models.FloatField(null=True, verbose_name=float)),
                ('superStateType', models.CharField(max_length=50, null=True)),
                ('superStateManufacturer', models.CharField(max_length=50, null=True)),
                ('substrateType', models.CharField(max_length=50, null=True)),
                ('substrateManufacturer', models.CharField(max_length=50, null=True)),
                ('frameType', models.CharField(max_length=50, null=True)),
                ('frameAdhesive', models.CharField(max_length=50, null=True)),
                ('encapsulateType', models.CharField(max_length=50, null=True)),
                ('encapsulantManufacturer', models.CharField(max_length=50, null=True)),
                ('junctionBoxType', models.CharField(max_length=50, null=True)),
                ('junctionBoxManufacturer', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestSequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequenceName', models.IntegerField(null=True, verbose_name=int)),
            ],
        ),
        migrations.CreateModel(
            name='TestStandard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standardName', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('publishedDate', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceName', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('isF1Required', models.CharField(max_length=3, null=True)),
                ('F1Frequency', models.FloatField(max_length=255, null=True)),
                ('standardID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.teststandard')),
            ],
        ),
        migrations.CreateModel(
            name='PerformanceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxSystemVoltage', models.FloatField(null=True, verbose_name=float)),
                ('voc', models.FloatField(max_length=50, null=True)),
                ('isc', models.FloatField(max_length=50, null=True)),
                ('vmp', models.FloatField(max_length=50, null=True)),
                ('imp', models.FloatField(max_length=50, null=True)),
                ('pmp', models.FloatField(max_length=50, null=True)),
                ('ff', models.FloatField(max_length=50, null=True)),
                ('modelNum', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.product')),
                ('sequenceId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.testsequence')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=255, null=True)),
                ('address2', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=20, null=True)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('fax', models.CharField(max_length=10, null=True)),
                ('clientID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.client')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('certNumber', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name=int)),
                ('certID', models.IntegerField(null=True, verbose_name=int)),
                ('reportNumber', models.IntegerField(null=True, verbose_name=int)),
                ('issueDate', models.DateField(null=True)),
                ('locationID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.location')),
                ('modelNum', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.product')),
                ('standardID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.teststandard')),
                ('userId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
    ]
