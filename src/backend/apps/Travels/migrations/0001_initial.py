# Generated by Django 2.1.7 on 2019-05-13 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
        ('Cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelAssociation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TravelGrouping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TravelGroupOwnership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TravelGroups',
            fields=[
                ('travel_group_id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('travel_group_note', models.TextField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Travels',
            fields=[
                ('travel_id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('visibility', models.CharField(choices=[('M', 'Only Me'), ('F', 'Friend'), ('P', 'Public')], default='F', max_length=1)),
                ('travel_note', models.TextField(max_length=140)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cities.Cities')),
            ],
        ),
        migrations.AddIndex(
            model_name='travelgroups',
            index=models.Index(fields=['travel_group_id'], name='TG_idx'),
        ),
        migrations.AddField(
            model_name='travelgroupownership',
            name='travel_group_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Travels.TravelGroups'),
        ),
        migrations.AddField(
            model_name='travelgroupownership',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Users'),
        ),
        migrations.AddField(
            model_name='travelgrouping',
            name='travel_group_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Travels.TravelGroups'),
        ),
        migrations.AddField(
            model_name='travelgrouping',
            name='travel_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Travels.Travels'),
        ),
        migrations.AddField(
            model_name='travelassociation',
            name='company_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_user_id', to='Users.Users'),
        ),
        migrations.AddField(
            model_name='travelassociation',
            name='travel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Travels.Travels'),
        ),
        migrations.AddIndex(
            model_name='travels',
            index=models.Index(fields=['travel_id'], name='T_travelid_idx'),
        ),
        migrations.AddIndex(
            model_name='travels',
            index=models.Index(fields=['date_start'], name='T_datestart_idx'),
        ),
        migrations.AddIndex(
            model_name='travels',
            index=models.Index(fields=['date_end'], name='T_dateend_idx'),
        ),
        migrations.AddIndex(
            model_name='travels',
            index=models.Index(fields=['city_id'], name='T_cityid_idx'),
        ),
        migrations.AddIndex(
            model_name='travels',
            index=models.Index(fields=['visibility'], name='T_visibility_idx'),
        ),
        migrations.AddIndex(
            model_name='travelgroupownership',
            index=models.Index(fields=['user_id'], name='TGO_userid_idx'),
        ),
        migrations.AddIndex(
            model_name='travelgroupownership',
            index=models.Index(fields=['travel_group_id'], name='TGO_travelgroupid_idx'),
        ),
        migrations.AddIndex(
            model_name='travelgrouping',
            index=models.Index(fields=['travel_id'], name='TG_travelid_idx'),
        ),
        migrations.AddIndex(
            model_name='travelgrouping',
            index=models.Index(fields=['travel_group_id'], name='TG_travelgroupid_idx'),
        ),
        migrations.AddIndex(
            model_name='travelassociation',
            index=models.Index(fields=['travel_id'], name='TA_travelid_idx'),
        ),
        migrations.AddIndex(
            model_name='travelassociation',
            index=models.Index(fields=['company_user_id'], name='TA_companyuserid_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='travelassociation',
            unique_together={('travel_id', 'company_user_id')},
        ),
    ]