# Generated by Django 5.1.1 on 2024-10-08 07:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bin', models.CharField(max_length=12)),
                ('industry', models.CharField(max_length=255)),
                ('higher_union_org', models.CharField(max_length=255)),
                ('union_name', models.CharField(max_length=255)),
                ('union_type', models.CharField(max_length=255)),
                ('addres', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('website', models.TextField()),
                ('email', models.CharField(max_length=255)),
                ('chairman_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vizit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vizit', models.BigIntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfCollegianBodies',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('body_type', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('union_ticket_number', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('prof_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prof_app.prof')),
            ],
        ),
        migrations.CreateModel(
            name='ProfMember',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('union_ticket_number', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('birth_date', models.DateField()),
                ('position', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=50)),
                ('total_work_experience', models.DateField()),
                ('org_work_experience', models.DateField()),
                ('union_membership_date', models.DateField()),
                ('awards_list', models.TextField()),
                ('vacation_list', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=255)),
                ('prof_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prof_app.prof')),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('award_type', models.CharField(max_length=255)),
                ('award_date', models.DateField()),
                ('prof_memeber_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prof_app.profmember')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('report_type', models.CharField(max_length=255)),
                ('creator', models.CharField(max_length=255)),
                ('document', models.TextField()),
                ('status', models.CharField(max_length=50)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('submission_date', models.DateField()),
                ('acceptance_date', models.DateField()),
                ('prof_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prof_app.prof')),
            ],
        ),
        migrations.CreateModel(
            name='SocialPartnershipAgreements',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('agreement_type', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('prof_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prof_app.prof')),
            ],
        ),
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sanatorium', models.CharField(max_length=255)),
                ('vacation_date', models.DateField()),
                ('prof_memeber_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prof_app.profmember')),
            ],
        ),
    ]
