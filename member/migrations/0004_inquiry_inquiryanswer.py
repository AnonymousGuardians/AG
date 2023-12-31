# Generated by Django 4.2.4 on 2023-08-22 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('inquiry_title', models.CharField(max_length=1024)),
                ('inquiry_content', models.ImageField(upload_to='Inquiry/%Y/%m/%d')),
                ('inquiry_status', models.SmallIntegerField(default=0)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
            options={
                'db_table': 'tbl_inquiry',
            },
        ),
        migrations.CreateModel(
            name='InquiryAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('inquiry_answer_content', models.CharField(max_length=1024)),
                ('funding_inquiry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.inquiry')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
            options={
                'db_table': 'tbl_inquiry_answer',
            },
        ),
    ]
