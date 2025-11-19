# En app_mascotas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_mascotas, name='inicio_mascotas'),
    
    # MASCOTAS
    path('mascota/ver/', views.ver_mascotas, name='ver_mascotas'),
    path('mascota/agregar/', views.agregar_mascota, name='agregar_mascota'),
    path('mascota/actualizar/<int:id>/', views.actualizar_mascota, name='actualizar_mascota'),
    path('mascota/borrar/<int:id>/', views.borrar_mascota, name='borrar_mascota'),
    
    # PRODUCTOS
    path('producto/ver/', views.ver_productos, name='ver_productos'),
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/borrar/<int:id>/', views.borrar_producto, name='borrar_producto'),
    
    # PROVEEDORES
    path('proveedor/ver/', views.ver_proveedores, name='ver_proveedores'),
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/actualizar/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/borrar/<int:id>/', views.borrar_proveedor, name='borrar_proveedor'),
    
    # CLIENTES
    path('cliente/ver/', views.ver_clientes, name='ver_clientes'),
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/actualizar/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),
    
    # EMPLEADOS
    path('empleado/ver/', views.ver_empleados, name='ver_empleados'),
    path('empleado/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleado/actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleado/borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),
    
    # VENTAS
    path('venta/ver/', views.ver_ventas, name='ver_ventas'),
    path('venta/agregar/', views.agregar_venta, name='agregar_venta'),
    path('venta/borrar/<int:id>/', views.borrar_venta, name='borrar_venta'),
    path('venta/detalle/<int:venta_id>/', views.ver_detalle_venta, name='ver_detalle_venta'),
]