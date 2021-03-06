# Generated by Django 2.2.9 on 2020-01-19 20:25

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('Description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_client', models.BooleanField(default=False, verbose_name='client status')),
                ('is_translator', models.BooleanField(default=False, verbose_name='translator status')),
                ('Nom', models.CharField(max_length=50)),
                ('Prénom', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=255)),
                ('Wilaya', models.CharField(max_length=20)),
                ('Commune', models.CharField(max_length=20)),
                ('Adresse', models.CharField(max_length=100)),
                ('Telephone', models.CharField(max_length=10)),
                ('Fax', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('General', 'General'), ('Scientifque', 'Scientifque'), ('Web', 'Web')], max_length=11)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('languages', models.ManyToManyField(to='Traduction.Language')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Devis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=False)),
                ('is_current', models.BooleanField(default=False)),
                ('is_assermented', models.BooleanField(default=False)),
                ('assertmente', models.FileField(null=True, upload_to='')),
                ('client', models.CharField(max_length=20)),
                ('nom', models.CharField(max_length=20, null=True)),
                ('prenom', models.CharField(max_length=20, null=True)),
                ('mail', models.EmailField(max_length=255, null=True)),
                ('adresse', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(choices=[('General', 'General'), ('Scientifque', 'Scientifque'), ('Web', 'Web')], max_length=11, null=True)),
                ('Zone', models.TextField(max_length=300, null=True)),
                ('fichier', models.FileField(upload_to='')),
                ('langues', models.ManyToManyField(to='Traduction.Language')),
                ('traducteur', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Devis',
            },
        ),
    ]
