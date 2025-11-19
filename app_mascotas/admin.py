from django.contrib import admin
from .models import Cliente, Empleado, Mascota, Producto, Proveedor, Venta, DetalleVenta

# =============================
# CLIENTE ADMIN
# =============================
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apepaterno', 'apematerno', 'telefono', 'tipo_mascota_preferida', 'id_empleado_atencion')
    list_filter = ('tipo_mascota_preferida', 'id_empleado_atencion')
    search_fields = ('nombre', 'apepaterno', 'apematerno', 'correo_electronico')
    list_per_page = 20

# =============================
# EMPLEADO ADMIN
# =============================
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apepaterno', 'apematerno', 'puesto', 'especialidad_mascotas', 'telefono')
    list_filter = ('puesto', 'especialidad_mascotas')
    search_fields = ('nombre', 'apepaterno', 'apematerno', 'puesto')
    list_per_page = 20

# =============================
# MASCOTA ADMIN
# =============================
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'edad', 'peso', 'id_cliente_propietario', 'id_empleado_cuidador')
    list_filter = ('especie', 'raza', 'id_empleado_cuidador')
    search_fields = ('nombre', 'especie', 'raza', 'id_cliente_propietario__nombre')
    list_per_page = 20

# =============================
# PROVEEDOR ADMIN
# =============================
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('compañia', 'telefono', 'tiempo_entrega_dias', 'especialidad_productos')
    list_filter = ('especialidad_productos', 'tiempo_entrega_dias')
    search_fields = ('compañia', 'especialidad_productos', 'licencia_sanitaria')
    list_per_page = 20

# =============================
# PRODUCTO ADMIN
# =============================
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'tipo_mascota', 'precio', 'stock', 'id_proveedor')
    list_filter = ('categoria', 'tipo_mascota', 'id_proveedor')
    search_fields = ('nombre', 'descripcion', 'categoria')
    list_editable = ('precio', 'stock')
    list_per_page = 20

# =============================
# DETALLE VENTA INLINE
# =============================
class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1
    readonly_fields = ('subtotal',)

    def subtotal(self, obj):
        return obj.subtotal()
    subtotal.short_description = 'Subtotal'

# =============================
# VENTA ADMIN
# =============================
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id_venta', 'fecha_venta', 'id_cliente', 'id_empleado', 'total')
    list_filter = ('fecha_venta', 'id_empleado')
    search_fields = ('id_cliente__nombre', 'id_empleado__nombre', 'id_venta')
    readonly_fields = ('fecha_venta', 'total')
    inlines = [DetalleVentaInline]
    list_per_page = 20

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('id_cliente', 'id_empleado')
        return self.readonly_fields

# =============================
# DETALLE VENTA ADMIN
# =============================
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('id_detalle', 'id_venta', 'id_producto', 'cantidad', 'precio_unitario', 'subtotal')
    list_filter = ('id_venta__fecha_venta',)
    search_fields = ('id_venta__id_venta', 'id_producto__nombre')
    readonly_fields = ('subtotal_display',)
    list_per_page = 20

    def subtotal_display(self, obj):
        return obj.subtotal()
    subtotal_display.short_description = 'Subtotal'

# =============================
# REGISTRO DE MODELOS
# =============================
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(DetalleVenta, DetalleVentaAdmin)