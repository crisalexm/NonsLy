# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Colegio(models.Model):
    col_id = models.AutoField(primary_key=True)
    rbd = models.IntegerField()
    nombre = models.CharField(max_length=50)
    sigla = models.CharField(max_length=5, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
class Alumno(models.Model):
    alum_id = models.AutoField(primary_key=True)
    rut = models.CharField(unique=True, max_length=10)
    nombre = models.CharField(max_length=50, db_collation='utf8mb3_general_ci')
    apellido1 = models.CharField(max_length=50, db_collation='utf8mb3_general_ci')
    apellido2 = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fechanacimiento = models.DateField(db_column='fechaNacimiento')  # Field name made lowercase.
    telefono = models.CharField(max_length=11, db_collation='utf8mb3_general_ci')
    email = models.CharField(unique=True, max_length=200)
    genero = models.CharField(max_length=10, db_collation='utf8mb3_general_ci')
    status = models.CharField(max_length=8, db_collation='utf8mb3_general_ci')

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()



class Apoderado(models.Model):
    apo_id = models.AutoField(primary_key=True)
    rut = models.CharField(unique=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50, blank=True, null=True)
    fechanacimiento = models.DateField(db_column='fechaNacimiento')  # Field name made lowercase.
    telefono = models.CharField(max_length=11)
    email = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()



class Asignatura(models.Model):
    asig_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    curso = models.OneToOneField('Curso', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Clase(models.Model):
    clase_id = models.AutoField(primary_key=True)
    asig = models.ForeignKey(Asignatura, models.DO_NOTHING)
    prof = models.ForeignKey('Profesor', models.DO_NOTHING)
    per = models.ForeignKey('Periodo', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()







class Curso(models.Model):
    curso_id = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    capacidad = models.PositiveIntegerField()
    niv = models.ForeignKey('Nivel', models.DO_NOTHING)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()







class Evaluacion(models.Model):
    eva_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    asig = models.ForeignKey(Asignatura, models.DO_NOTHING, to_field='curso_id')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()



class Nivel(models.Model):
    niv_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Nota(models.Model):
    nota_id = models.AutoField(primary_key=True)
    noobtenida = models.DecimalField(db_column='noObtenida', max_digits=3, decimal_places=2)  # Field name made lowercase.
    alum = models.ForeignKey(Alumno, models.DO_NOTHING)
    prof = models.ForeignKey('Profesor', models.DO_NOTHING)
    eva = models.ForeignKey(Evaluacion, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()



class Periodo(models.Model):
    per_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    fechainicio = models.DateField(db_column='fechaInicio')  # Field name made lowercase.
    fechafin = models.DateField(db_column='fechaFin')  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Profesor(models.Model):
    prof_id = models.AutoField(primary_key=True)
    rut = models.CharField(unique=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50, blank=True, null=True)
    fechanacimiento = models.DateField(db_column='fechaNacimiento')  # Field name made lowercase.
    telefono = models.CharField(max_length=11)
    email = models.CharField(unique=True, max_length=200)
    genero = models.CharField(max_length=10)
    especialidad = models.CharField(max_length=50, blank=True, null=True)
   
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

