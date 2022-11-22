# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    col_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'alumno'


class AlumnoApoderado(models.Model):
    alumno_apoderado_id = models.AutoField(primary_key=True)
    alum = models.ForeignKey(Alumno, models.DO_NOTHING)
    apo = models.ForeignKey('Apoderado', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'alumno_apoderado'


class AlumnoClase(models.Model):
    alumno_clase_id = models.AutoField(primary_key=True)
    alum = models.ForeignKey(Alumno, models.DO_NOTHING)
    clase = models.ForeignKey('Clase', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'alumno_clase'


class AlumnoCurso(models.Model):
    alumno_curso_id = models.AutoField(primary_key=True)
    alum = models.ForeignKey(Alumno, models.DO_NOTHING)
    curso = models.ForeignKey('Curso', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'alumno_curso'


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

    class Meta:
        managed = False
        db_table = 'apoderado'


class Asignatura(models.Model):
    asig_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    curso = models.OneToOneField('Curso', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'asignatura'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Clase(models.Model):
    clase_id = models.AutoField(primary_key=True)
    asig = models.ForeignKey(Asignatura, models.DO_NOTHING)
    prof = models.ForeignKey('Profesor', models.DO_NOTHING)
    per = models.ForeignKey('Periodo', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clase'


class Colegio(models.Model):
    col_id = models.AutoField(primary_key=True)
    rbd = models.IntegerField()
    nombre = models.CharField(max_length=50)
    sigla = models.CharField(max_length=5, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'colegio'


class ColegioProfesor(models.Model):
    colegio_profesor_id = models.AutoField(primary_key=True)
    col = models.ForeignKey(Colegio, models.DO_NOTHING)
    prof = models.ForeignKey('Profesor', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'colegio_profesor'


class Curso(models.Model):
    curso_id = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    capacidad = models.PositiveIntegerField()
    niv = models.ForeignKey('Nivel', models.DO_NOTHING)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'curso'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Evaluacion(models.Model):
    eva_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    asig = models.ForeignKey(Asignatura, models.DO_NOTHING, to_field='curso_id')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'evaluacion'


class Nivel(models.Model):
    niv_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nivel'


class Nota(models.Model):
    nota_id = models.AutoField(primary_key=True)
    noobtenida = models.DecimalField(db_column='noObtenida', max_digits=3, decimal_places=2)  # Field name made lowercase.
    alum = models.ForeignKey(Alumno, models.DO_NOTHING)
    prof = models.ForeignKey('Profesor', models.DO_NOTHING)
    eva = models.ForeignKey(Evaluacion, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nota'


class Periodo(models.Model):
    per_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    fechainicio = models.DateField(db_column='fechaInicio')  # Field name made lowercase.
    fechafin = models.DateField(db_column='fechaFin')  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'periodo'


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

    class Meta:
        managed = False
        db_table = 'profesor'
