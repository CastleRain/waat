# Generated by Django 4.0.1 on 2022-01-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundingapp', '0006_delete_fundingboards_delete_post_delete_fundingfunc'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinProject',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=30)),
                ('board_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=30)),
                ('user_email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
            options={
                'db_table': 'JoinProject',
                'managed': False,
            },
        ),
    ]