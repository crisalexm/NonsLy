from django.db import models
import datetime
# Create your models here.

class Colegio(models.Model):
    col_id = models.AutoField(primary_key=True)
    rbd = models.IntegerField()
    nombre = models.CharField(max_length=50, help_text="Ingrese nombre del colegio.")
    sigla = models.CharField(max_length=5, blank=True, null=True)
    direccion=models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=["created_at"]
        db_table='colegio'
        verbose_name_plural='Colegios'
        
    def __str__(self):
        return "%s %s " %(self.nombre, self.sigla)
    
class Profesor(models.Model):
    MASCULINO = 'Masculino'
    FEMENINO = 'Femenino'
    OTRO = 'Otro'
    GENEROS = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
        (OTRO, 'Otro'),
    ]
    prof_id = models.AutoField(primary_key=True)
    rut = models.CharField(unique=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(db_column='fechaNacimiento')  # Field name made lowercase.
    telefono = models.CharField(max_length=11)
    email = models.EmailField(unique=True, max_length=200)
    genero = models.CharField(max_length=10,  choices=GENEROS)
    especialidad = models.CharField(max_length=50, blank=True, null=True)
    
    colegio=models.ManyToManyField(Colegio, max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["created_at"]
        db_table='profesor'
        verbose_name_plural='Profesores'
        
    def __str__(self):
        return "%s %s - %s" %(self.nombre, self.apellido1, self.email)
    
class Alumno(models.Model):
    ACTIVO = 'Activo'
    INACTIVO = 'Inactivo'
    ESTADOS =[
        (ACTIVO,'Activo'),
        (INACTIVO,'Inactivo'),
        ]
    
    MASCULINO = 'Masculino'
    FEMENINO = 'Femenino'
    OTRO = 'Otro'
    GENEROS = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
        (OTRO, 'Otro'),
    ]
    
    
    alum_id = models.AutoField(primary_key=True)
    rut = models.CharField(unique=True, max_length=10)
    nombre = models.CharField(max_length=50, db_collation='utf8mb3_general_ci')
    apellido1 = models.CharField(max_length=50, db_collation='utf8mb3_general_ci')
    apellido2 = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    fecha_nacimiento = models.DateField(db_column='fechaNacimiento')  # Field name made lowercase.
    telefono = models.CharField(max_length=11, db_collation='utf8mb3_general_ci')
    email = models.CharField(unique=True, max_length=200)
    genero = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', choices=GENEROS)
    
    status = models.CharField(max_length=8, db_collation='utf8mb3_general_ci', choices=ESTADOS)
    
    curso=models.ForeignKey('Curso',  on_delete=models.SET_NULL, null=True)
    colegio=models.ForeignKey(Colegio,  on_delete=models.SET_NULL, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s - %s" %(self.nombre, self.apellido1, self.email)
    class Meta:
        
        ordering=["created_at"]
        db_table = 'alumno'
        verbose_name_plural='Alumnos'


class Apoderado(models.Model):
    MASCULINO = 'Masculino'
    FEMENINO = 'Femenino'
    OTRO = 'Otro'
    GENEROS = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
        (OTRO, 'Otro'),
    ]
    
    apo_id = models.AutoField(primary_key=True)
    rut = models.CharField(unique=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(db_column='fechaNacimiento')  # Field name made lowercase.
    telefono = models.CharField(max_length=11)
    email = models.CharField(unique=True, max_length=200)
    genero = models.CharField(max_length=10, db_collation='utf8mb3_general_ci', choices=GENEROS)
    
    alumno=models.ManyToManyField(Alumno)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return "%s %s - %s" %(self.nombre, self.apellido1, self.email)
    class Meta:
        
        ordering=["created_at"]
        db_table = 'apoderado'    
        verbose_name_plural='Apoderados'
        
class Curso(models.Model):
    YEAR_CHOICES = []
    
    for r in range(2000, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
        
    curso_id = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    capacidad = models.PositiveIntegerField()
    nivel = models.ForeignKey('Nivel', on_delete=models.SET_NULL, null=True)
    annio_academico=models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year,verbose_name="Año académico")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" %(self.nombre, self.curso_id)
    class Meta:
        ordering=["nivel"]
        db_table = 'curso'
        verbose_name_plural="Cursos"
        

class Nivel(models.Model):
    niv_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre}'
    class Meta:
        
        ordering=["created_at"]
        db_table = 'nivel'
        verbose_name_plural='Niveles'


class Asignatura(models.Model):
    asig_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    codigo=models.CharField(max_length=5,unique=True)
    
    curso=models.ForeignKey(Curso, models.DO_NOTHING)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["nombre"]
        verbose_name_plural='Asignaturas'
        db_table = 'asignatura'     

class Periodo(models.Model):
    per_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    fecha_inicio = models.DateField()  # Field name made lowercase.
    fecha_fin = models.DateField()  # Field name made lowercase.
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Periodos'
        ordering=["nombre"]
        db_table = 'periodo'
     
class Evaluacion(models.Model):
    eva_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    
    asignatura = models.ForeignKey(Asignatura, models.DO_NOTHING)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Evaluaciones'
        ordering=["nombre"]
        db_table = 'evaluacion'
        
class Clase(models.Model):
    clase_id = models.AutoField(primary_key=True)
    asig = models.ForeignKey(Asignatura, models.DO_NOTHING)
    prof = models.ForeignKey(Profesor, models.DO_NOTHING)
    
    per = models.ForeignKey(Periodo, models.DO_NOTHING)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        
        verbose_name_plural='Clases'
        ordering=["created_at"]
        db_table = 'clase'
        
class Nota(models.Model):
    nota_id = models.AutoField(primary_key=True)
    nota_obtenida = models.DecimalField(max_digits=3, decimal_places=2)  # Field name made lowercase.
    
    alum = models.ForeignKey(Alumno, models.DO_NOTHING)
    prof = models.ForeignKey(Profesor, models.DO_NOTHING)
    eva = models.ForeignKey(Evaluacion, models.DO_NOTHING)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Notas'
        ordering=["created_at"]
        db_table = 'nota'