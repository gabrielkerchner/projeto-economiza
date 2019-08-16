# Generated by Django 2.1 on 2019-08-12 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_nome', models.CharField(choices=[['1', 'Lazer'], ['2', 'Transporte'], ['3', 'Alimentação'], ['4', 'Despesas do Lar'], ['5', 'Outros']], max_length=1)),
                ('limite_categoria', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_da_compra', models.DateTimeField(auto_now_add=True, verbose_name='Data da compra')),
                ('descricao', models.CharField(max_length=150)),
                ('preco', models.FloatField()),
                ('quantidade', models.PositiveIntegerField()),
                ('esta_pago', models.BooleanField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gasto', to='economiza.Categoria')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gasto', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('sobrenome', models.CharField(max_length=128)),
                ('sexo', models.CharField(choices=[['F', 'Feminino'], ['M', 'Masculino'], ['N', 'Nenhuma das opções']], max_length=1)),
                ('idade', models.IntegerField(null=True)),
                ('telefone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('limite', models.PositiveIntegerField(null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfis',
                'ordering': ['criado_em'],
            },
        ),
    ]