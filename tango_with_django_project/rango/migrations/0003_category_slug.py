from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]