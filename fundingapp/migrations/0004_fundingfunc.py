# Generated by Django 4.0.1 on 2022-01-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundingapp', '0003_joinfund_user1_post_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundingFunc',
            fields=[
                ('board_id', models.IntegerField(primary_key=True, serialize=False)),
                ('func_a_expl', models.CharField(max_length=50)),
                ('func_b_expl', models.CharField(max_length=50)),
                ('func_c_expl', models.CharField(max_length=50)),
                ('func_a_price', models.IntegerField()),
                ('func_b_price', models.IntegerField()),
                ('func_c_price', models.IntegerField()),
            ],
            options={
                'db_table': 'FundingFunc',
                'managed': False,
            },
        ),
    ]