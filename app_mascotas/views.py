from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota, Producto, Proveedor, Cliente, Empleado, Venta, DetalleVenta

def inicio_mascotas(request):
    total_mascotas = Mascota.objects.count()
    total_productos = Producto.objects.count()
    total_proveedores = Proveedor.objects.count()
    total_clientes = Cliente.objects.count()
    total_empleados = Empleado.objects.count()
    total_ventas = Venta.objects.count()

    mascotas = Mascota.objects.all().order_by('nombre')[:5]
    productos = Producto.objects.all().order_by('nombre')[:4]
    proveedores = Proveedor.objects.all().order_by('compañia')[:4]
    clientes = Cliente.objects.all().order_by('nombre')[:4]
    empleados = Empleado.objects.all().order_by('nombre')[:4]
    ventas = Venta.objects.all().order_by('-fecha_venta')[:4]

    return render(request, 'inicio.html', {
        'total_mascotas': total_mascotas,
        'total_productos': total_productos,
        'total_proveedores': total_proveedores,
        'total_clientes': total_clientes,
        'total_empleados': total_empleados,
        'total_ventas': total_ventas,
        'mascotas': mascotas,
        'productos': productos,
        'proveedores': proveedores,
        'clientes': clientes,
        'empleados': empleados,
        'ventas': ventas,
    })

# =============================
# MASCOTAS
# =============================
def ver_mascotas(request):
    mascotas = Mascota.objects.all().order_by('nombre')
    return render(request, 'mascota/ver_mascotas.html', {'mascotas': mascotas})

def agregar_mascota(request):
    empleados = Empleado.objects.all()
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        Mascota.objects.create(
            nombre=request.POST.get('nombre'),
            edad=request.POST.get('edad'),
            peso=request.POST.get('peso'),
            cuidados_especiales=request.POST.get('cuidados_especiales'),
            enfermedades=request.POST.get('enfermedades'),
            especie=request.POST.get('especie'),
            raza=request.POST.get('raza'),
            alimentacion_recomendada=request.POST.get('alimentacion_recomendada'),
            id_empleado_cuidador_id=request.POST.get('empleado_cuidador'),
            id_cliente_propietario_id=request.POST.get('cliente_propietario')
        )
        return redirect('ver_mascotas')
    
    return render(request, 'mascota/agregar_mascota.html', {
        'empleados': empleados,
        'clientes': clientes
    })

def actualizar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id_mascota=id)  # ← CAMBIADO: id_mascota
    empleados = Empleado.objects.all()
    clientes = Cliente.objects.all()
    
    if request.method == 'POST':
        mascota.nombre = request.POST.get('nombre')
        mascota.edad = request.POST.get('edad')
        mascota.peso = request.POST.get('peso')
        mascota.cuidados_especiales = request.POST.get('cuidados_especiales')
        mascota.enfermedades = request.POST.get('enfermedades')
        mascota.especie = request.POST.get('especie')
        mascota.raza = request.POST.get('raza')
        mascota.alimentacion_recomendada = request.POST.get('alimentacion_recomendada')
        mascota.id_empleado_cuidador_id = request.POST.get('empleado_cuidador')
        mascota.id_cliente_propietario_id = request.POST.get('cliente_propietario')
        mascota.save()
        return redirect('ver_mascotas')
    
    return render(request, 'mascota/actualizar_mascota.html', {
        'mascota': mascota,
        'empleados': empleados,
        'clientes': clientes
    })

def borrar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id_mascota=id)  # ← CAMBIADO: id_mascota
    if request.method == 'POST':
        mascota.delete()
        return redirect('ver_mascotas')
    return render(request, 'mascota/borrar_mascota.html', {'mascota': mascota})

# =============================
# PRODUCTOS
# =============================
def ver_productos(request):
    productos = Producto.objects.all().order_by('nombre')
    return render(request, 'producto/ver_productos.html', {'productos': productos})

def agregar_producto(request):
    proveedores = Proveedor.objects.all()

    if request.method == 'POST':
        Producto.objects.create(
            nombre=request.POST.get('nombre'),
            precio=request.POST.get('precio'),
            categoria=request.POST.get('categoria'),
            garantia_meses=request.POST.get('garantia_meses'),
            descripcion=request.POST.get('descripcion'),
            stock=request.POST.get('stock'),
            tipo_mascota=request.POST.get('tipo_mascota'),
            id_proveedor_id=request.POST.get('proveedor')
        )
        return redirect('ver_productos')

    return render(request, 'producto/agregar_producto.html', {
        'proveedores': proveedores
    })

def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)  # ← CAMBIADO: id_producto
    proveedores = Proveedor.objects.all()
    
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.precio = request.POST.get('precio')
        producto.categoria = request.POST.get('categoria')
        producto.garantia_meses = request.POST.get('garantia_meses')
        producto.descripcion = request.POST.get('descripcion')
        producto.stock = request.POST.get('stock')
        producto.tipo_mascota = request.POST.get('tipo_mascota')
        producto.id_proveedor_id = request.POST.get('proveedor')
        producto.save()
        return redirect('ver_productos')
    
    return render(request, 'producto/actualizar_producto.html', {
        'producto': producto,
        'proveedores': proveedores
    })

def borrar_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)  # ← CAMBIADO: id_producto
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})

# =============================
# PROVEEDORES
# =============================
def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

def agregar_proveedor(request):
    if request.method == 'POST':
        Proveedor.objects.create(
            compañia=request.POST.get('compañia'),
            telefono=request.POST.get('telefono'),
            tiempo_entrega_dias=request.POST.get('tiempo_entrega_dias'),
            licencia_sanitaria=request.POST.get('licencia_sanitaria'),
            especialidad_productos=request.POST.get('especialidad_productos')
        )
        return redirect('ver_proveedores')
    return render(request, 'proveedor/agregar_proveedor.html')

def actualizar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id_compañia=id)  # ← CAMBIADO: id_compañia
    if request.method == 'POST':
        proveedor.compañia = request.POST.get('compañia')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.tiempo_entrega_dias = request.POST.get('tiempo_entrega_dias')
        proveedor.licencia_sanitaria = request.POST.get('licencia_sanitaria')
        proveedor.especialidad_productos = request.POST.get('especialidad_productos')
        proveedor.save()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def borrar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id_compañia=id)  # ← CAMBIADO: id_compañia
    if request.method == "POST":
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, "proveedor/borrar_proveedor.html", {"proveedor": proveedor})

# =============================
# CLIENTES
# =============================
def ver_clientes(request):
    clientes = Cliente.objects.all().order_by('nombre')
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    empleados = Empleado.objects.all()
    
    if request.method == 'POST':
        Cliente.objects.create(
            nombre=request.POST.get('nombre'),
            apepaterno=request.POST.get('apepaterno'),
            apematerno=request.POST.get('apematerno'),
            telefono=request.POST.get('telefono'),
            domicilio=request.POST.get('domicilio'),
            correo_electronico=request.POST.get('correo_electronico'),
            tipo_mascota_preferida=request.POST.get('tipo_mascota_preferida'),
            id_empleado_atencion_id=request.POST.get('empleado_atencion')
        )
        return redirect('ver_clientes')
    
    return render(request, 'cliente/agregar_cliente.html', {
        'empleados': empleados
    })

def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)  # ← CAMBIADO: id_cliente
    empleados = Empleado.objects.all()
    
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apepaterno = request.POST.get('apepaterno')
        cliente.apematerno = request.POST.get('apematerno')
        cliente.telefono = request.POST.get('telefono')
        cliente.domicilio = request.POST.get('domicilio')
        cliente.correo_electronico = request.POST.get('correo_electronico')
        cliente.tipo_mascota_preferida = request.POST.get('tipo_mascota_preferida')
        cliente.id_empleado_atencion_id = request.POST.get('empleado_atencion')
        cliente.save()
        return redirect('ver_clientes')
    
    return render(request, 'cliente/actualizar_cliente.html', {
        'cliente': cliente,
        'empleados': empleados
    })

def borrar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)  # ← CAMBIADO: id_cliente
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# =============================
# EMPLEADOS
# =============================
def ver_empleados(request):
    empleados = Empleado.objects.all().order_by('nombre')
    return render(request, 'empleado/ver_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        Empleado.objects.create(
            nombre=request.POST.get('nombre'),
            apepaterno=request.POST.get('apepaterno'),
            apematerno=request.POST.get('apematerno'),
            telefono=request.POST.get('telefono'),
            domicilio=request.POST.get('domicilio'),
            puesto=request.POST.get('puesto'),
            especialidad_mascotas=request.POST.get('especialidad_mascotas')
        )
        return redirect('ver_empleados')
    return render(request, 'empleado/agregar_empleado.html')

def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id_empleado=id)  # ← CAMBIADO: id_empleado
    if request.method == 'POST':
        empleado.nombre = request.POST.get('nombre')
        empleado.apepaterno = request.POST.get('apepaterno')
        empleado.apematerno = request.POST.get('apematerno')
        empleado.telefono = request.POST.get('telefono')
        empleado.domicilio = request.POST.get('domicilio')
        empleado.puesto = request.POST.get('puesto')
        empleado.especialidad_mascotas = request.POST.get('especialidad_mascotas')
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})

def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id_empleado=id)  # ← CAMBIADO: id_empleado
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})

# =============================
# VENTAS
# =============================
def ver_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'venta/ver_ventas.html', {'ventas': ventas})

def agregar_venta(request):
    empleados = Empleado.objects.all()
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()

    if request.method == 'POST':
        # Crear la venta principal
        venta = Venta.objects.create(
            fecha_venta=request.POST.get('fecha_venta'),
            total=0,  # Se calculará con los detalles
            id_cliente_id=request.POST.get('cliente'),
            id_empleado_id=request.POST.get('empleado')
        )

        # Procesar productos seleccionados
        productos_ids = request.POST.getlist('productos')
        cantidades = request.POST.getlist('cantidades')
        
        total_venta = 0
        for i, producto_id in enumerate(productos_ids):
            producto = get_object_or_404(Producto, id_producto=producto_id)  # ← CAMBIADO
            cantidad = int(cantidades[i])
            precio_unitario = producto.precio
            
            DetalleVenta.objects.create(
                id_venta=venta,
                id_producto=producto,
                cantidad=cantidad,
                precio_unitario=precio_unitario
            )
            
            total_venta += cantidad * precio_unitario
            
            # Actualizar stock
            producto.stock -= cantidad
            producto.save()

        # Actualizar total de la venta
        venta.total = total_venta
        venta.save()

        return redirect('ver_ventas')

    return render(request, 'venta/agregar_venta.html', {
        'empleados': empleados,
        'clientes': clientes,
        'productos': productos
    })

def borrar_venta(request, id):
    venta = get_object_or_404(Venta, id_venta=id)  # ← CAMBIADO: id_venta
    if request.method == 'POST':
        # Restaurar stock antes de eliminar
        detalles = DetalleVenta.objects.filter(id_venta=venta)
        for detalle in detalles:
            producto = detalle.id_producto
            producto.stock += detalle.cantidad
            producto.save()
        
        venta.delete()
        return redirect('ver_ventas')
    return render(request, 'venta/borrar_venta.html', {'venta': venta})

# =============================
# DETALLE VENTAS
# =============================
def ver_detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, id_venta=venta_id)  # ← CAMBIADO: id_venta
    detalles = DetalleVenta.objects.filter(id_venta=venta)
    return render(request, 'venta/ver_detalle_venta.html', {
        'venta': venta,
        'detalles': detalles
    })