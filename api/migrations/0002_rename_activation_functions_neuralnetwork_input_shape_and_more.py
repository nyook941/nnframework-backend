# Generated by Django 5.1.1 on 2024-10-20 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="neuralnetwork",
            old_name="activation_functions",
            new_name="input_shape",
        ),
        migrations.RenameField(
            model_name="neuralnetwork",
            old_name="layer_types",
            new_name="layers",
        ),
        migrations.RemoveField(
            model_name="neuralnetwork",
            name="num_layers",
        ),
    ]
