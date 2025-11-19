from django.db import models

# =============================
# CLIENTE
# =============================
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    apepaterno = models.CharField(max_length=50)
    apematerno = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    domicilio = models.TextField()
    correo_electronico = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20)
    tipo_mascota_preferida = models.CharField(max_length=50, blank=True, null=True)
    id_empleado_atencion = models.ForeignKey('Empleado', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apepaterno} {self.apematerno}"

    class Meta:
        db_table = 'clientes'


# =============================
# EMPLEADO
# =============================
class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    apepaterno = models.CharField(max_length=50)
    apematerno = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)
    domicilio = models.TextField()
    puesto = models.CharField(max_length=50)
    especialidad_mascotas = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apepaterno} - {self.puesto}"

    class Meta:
        db_table = 'empleados'


# =============================
# MASCOTA
# =============================
class Mascota(models.Model):
    ESPECIES_CHOICES = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('ave', 'Ave'),
        ('roedor', 'Roedor'),
        ('reptil', 'Reptil'),
        ('pez', 'Pez'),
        ('otro', 'Otro'),
    ]

    id_mascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    peso = models.DecimalField(max_digits=4, decimal_places=2)
    cuidados_especiales = models.CharField(max_length=250, blank=True, null=True)
    enfermedades = models.CharField(max_length=200, blank=True, null=True)
    especie = models.CharField(max_length=50, choices=ESPECIES_CHOICES)
    raza = models.CharField(max_length=50, blank=True, null=True)
    alimentacion_recomendada = models.CharField(max_length=50, blank=True, null=True)
    id_empleado_cuidador = models.ForeignKey('Empleado', on_delete=models.SET_NULL, null=True, blank=True, related_name='mascotas_cuidadas')
    id_cliente_propietario = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='mascotas')

    def __str__(self):
        return f"{self.nombre} - {self.especie}"

    class Meta:
        db_table = 'mascotas'


# =============================
# PROVEEDOR
# =============================
class Proveedor(models.Model):
    id_compañia = models.AutoField(primary_key=True)
    compañia = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    tiempo_entrega_dias = models.IntegerField(default=1)
    licencia_sanitaria = models.CharField(max_length=250, unique=True)
    especialidad_productos = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.compañia

    class Meta:
        db_table = 'proveedores'


# =============================
# PRODUCTO
# =============================
class Producto(models.Model):
    CATEGORIA_CHOICES = [
        ('alimento', 'Alimento'),
        ('juguete', 'Juguete'),
        ('accesorio', 'Accesorio'),
        ('higiene', 'Higiene y Cuidado'),
        ('salud', 'Salud'),
        ('transporte', 'Transporte'),
    ]
    
    TIPO_MASCOTA_CHOICES = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('ave', 'Ave'),
        ('roedor', 'Roedor'),
        ('reptil', 'Reptil'),
        ('pez', 'Pez'),
        ('universal', 'Universal'),
    ]

    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)
    garantia_meses = models.IntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)
    stock = models.IntegerField(default=0)
    tipo_mascota = models.CharField(max_length=50, choices=TIPO_MASCOTA_CHOICES, default='universal')
    id_proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.get_tipo_mascota_display()}"

    class Meta:
        db_table = 'productos'


# =============================
# VENTA
# =============================
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    id_empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta {self.id_venta} - {self.fecha_venta.strftime('%Y-%m-%d')}"

    class Meta:
        db_table = 'ventas'


# =============================
# DETALLE VENTA
# =============================
class DetalleVenta(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey('Venta', on_delete=models.CASCADE, related_name='detalles')
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Detalle {self.id_detalle} - Venta {self.id_venta.id_venta}"

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    class Meta:
        db_table = 'detalle_ventas'