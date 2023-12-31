# Generated by Django 4.2.4 on 2023-08-20 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.SmallIntegerField(default=0)),
                ('started_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('ends_on', models.DateTimeField(auto_now=True, null=True)),
                ('campaign_title', models.CharField(max_length=256)),
                ('campaign_category', models.CharField(max_length=100)),
                ('campaign_description1', models.CharField(max_length=100)),
                ('campaign_description2', models.CharField(max_length=100)),
                ('campaign_description3', models.CharField(max_length=100)),
                ('campaign_status', models.SmallIntegerField(default=0)),
                ('campaign_image', models.ImageField(upload_to='Campaign/%Y/%m/%d')),
                ('campaign_content', models.CharField(max_length=10240)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
            options={
                'db_table': 'tbl_campaign',
            },
        ),
        migrations.RemoveField(
            model_name='campaignheader',
            name='member_id',
        ),
        migrations.DeleteModel(
            name='CampaignDetail',
        ),
        migrations.AlterField(
            model_name='campaigninquiry',
            name='campaign_header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaign'),
        ),
        migrations.AlterField(
            model_name='campaignparticipant',
            name='campaign_header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaign'),
        ),
        migrations.AlterField(
            model_name='campaignphoto',
            name='campaign_header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaign'),
        ),
        migrations.AlterField(
            model_name='campaignreview',
            name='campaign_header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaign'),
        ),
        migrations.DeleteModel(
            name='CampaignHeader',
        ),
    ]
