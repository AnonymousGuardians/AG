# Generated by Django 4.2.4 on 2023-08-23 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0002_safetyscoreheader'),
        ('campaign', '0003_rename_campaign_header_campaigninquiry_campaign_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='city_detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='region.citydetail'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='city_header',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='region.cityheader'),
        ),
    ]
