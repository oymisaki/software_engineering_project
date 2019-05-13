# Generated by Django 2.1.7 on 2019-05-13 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendRelations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_user_note', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_name', models.CharField(max_length=20)),
                ('pswd_hash', models.BinaryField(editable=True, max_length=16)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown'), ('O', 'Other')], default='U', max_length=1)),
                ('resident_city_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='resident_city_id', to='Cities.Cities')),
            ],
        ),
        migrations.AddField(
            model_name='friendrelations',
            name='friend_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_user_id', to='Users.Users'),
        ),
        migrations.AddField(
            model_name='friendrelations',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_user_id', to='Users.Users'),
        ),
        migrations.AddIndex(
            model_name='users',
            index=models.Index(fields=['user_id'], name='U_userid_idx'),
        ),
        migrations.AddIndex(
            model_name='users',
            index=models.Index(fields=['email'], name='U_email_idx'),
        ),
        migrations.AddIndex(
            model_name='friendrelations',
            index=models.Index(fields=['user_id'], name='FR_userid_idx'),
        ),
        migrations.AddIndex(
            model_name='friendrelations',
            index=models.Index(fields=['user_id', 'friend_user_id'], name='FR_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='friendrelations',
            unique_together={('user_id', 'friend_user_id')},
        ),
    ]