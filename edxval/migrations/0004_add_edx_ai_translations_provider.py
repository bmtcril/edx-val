# Generated by Django 4.2.16 on 2024-11-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edxval', '0003_delete_transcriptcredentials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videotranscript',
            name='provider',
            field=models.CharField(choices=[('Custom', 'Custom'), ('3PlayMedia', '3PlayMedia'), ('Cielo24', 'Cielo24'), ('edx_ai_translations', 'edx_ai_translations')], default='Custom', max_length=30),
        ),
    ]