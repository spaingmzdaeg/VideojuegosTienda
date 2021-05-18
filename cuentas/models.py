from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cliente(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    primer_nombre = models.CharField(max_length=200)
    segundo_nombre = models.CharField(max_length=200,blank=True)
    primer_apellido = models.CharField(max_length=200)
    segundo_apellido = models.CharField(max_length=200,blank=True)
    email = models.EmailField()
    telefono = models.BigIntegerField(null=True,blank=True)
    perfil_foto = models.ImageField(default="user.png",null=True,blank=True,upload_to='fotosperfil')
    fecha_creacion = models.DateTimeField(auto_now_add=True,null=True)
    

    def __str__(self):
        return self.primer_nombre+" "+self.primer_apellido


class Tag(models.Model):
    nombre = models.CharField(max_length=200)
    

    def __str__(self):
        return self.nombre  



class Videojuego(models.Model):
    caratula = models.ImageField(upload_to='caratulas')
    nombre = models.CharField(max_length=200)
    PLAYSTATION5 = 'PlayStation 5'
    XBOXSERIES = 'XBOX Series'
    PLAYSTATION4 = 'PlayStation 4'
    XBOXONE = 'Xbox ONE'
    COMPUTADORA = 'PC'
    NINTENDOSWITCH = 'Nintendo Switch'
    ELECCION_PLATAFORMA = [
        (PLAYSTATION5,'PlayStation 5'),
        (XBOXSERIES,'XBOX Series'),
        (PLAYSTATION4,'PlayStation 4'),
        (XBOXONE,'XBOXONE'),
        (COMPUTADORA,'PC'),
        (NINTENDOSWITCH,'Nintendo Switch'),
    ]
    plataforma = models.CharField(max_length=50,
    choices=ELECCION_PLATAFORMA,
    default=PLAYSTATION4)
    ACCIONYAVENTURAS = 'Accion y Aventuras'
    JUEGOSMESA = 'Juegos de Mesa'
    FAMILIAR = 'Familiar'
    LUCHA = 'Lucha'
    PLATAFORMAS = 'Plataformas'
    PUZZLES = 'Puzzles'
    CARRERAS = 'Carreras'
    JUEGOSROL = 'Juegos de Rol'
    TIROS = 'FPS'
    SIMULACION = 'Simulacion'
    DEPORTES = 'Deportes'
    ESTRATEGIA = 'Estrategia'
    ELECCION_GENERO = [
        (ACCIONYAVENTURAS,'Accion y Aventuras'),
        (JUEGOSMESA,'Juegos de Mesa'),
        (FAMILIAR , 'Familiar'),
        (LUCHA , 'Lucha'),
        (PLATAFORMAS , 'Plataformas'),
        (PUZZLES , 'Puzzles'),
        (CARRERAS , 'Carreras'),
        (JUEGOSROL , 'Juegos de Rol'),
        (TIROS , 'FPS'),
        (SIMULACION , 'Simulacion'),
        (DEPORTES , 'Deportes'),
        (ESTRATEGIA , 'Estrategia'),
    ]
    genero = models.CharField(max_length=50,
    choices=ELECCION_GENERO,
    default=ACCIONYAVENTURAS)
    TODOS = 'E'
    TODOS10 = 'E+10'
    ADOLESCENTES = 'T'
    ADULTOS = 'M'
    PENDIENTE = 'RP'
    ELECCION_CLASIFICACION = [
        (TODOS , 'TODOS'),
        (TODOS10,'TODOS+10'),
        (ADOLESCENTES,'ADOLESCENTES'),
        (ADULTOS,'ADULTOS'),
        (PENDIENTE,'PENDIENTE'),
    ]
    clasificacion = models.CharField(max_length=50,
    choices=ELECCION_CLASIFICACION,
    default=TODOS,blank=True)
    descripcion = models.CharField(max_length=200,blank=True)
    fecha_lanzamiento = models.DateTimeField(blank=True)
    precio = models.FloatField(blank=True)
    tags = models.ManyToManyField(Tag)
    stock = models.IntegerField(blank=True)

    def __str__(self):
        return self.nombre+"-"+self.plataforma


class Pedido(models.Model):
    #cliente
    #videojuego
    ESTATUS = (
        ('PENDIENTE','PENDIENTE'),
        ('NO DISPONIBLE','NO DISPONIBLE'),
        ('ENTREGADO','ENTREGADO'),
    )
    cliente = models.ForeignKey(Cliente,null=True,on_delete = models.SET_NULL)
    videojuego = models.ForeignKey(Videojuego,null=True,on_delete = models.SET_NULL)
    fecha_pedido = models.DateTimeField(auto_now_add=True,null=True)
    estatus = models.CharField(max_length=200,null=True,choices=ESTATUS)
    nota = models.CharField(max_length=1000,null=True)


    def __str__(self):
        return self.videojuego.nombre+"-"+self.videojuego.plataforma+"-"+self.cliente.primer_nombre+" "+self.cliente.primer_apellido
    