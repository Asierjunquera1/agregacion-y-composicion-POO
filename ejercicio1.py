class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []

    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)


class Empleado:
    def __init__(self, nombre, empresa):
        self.nombre = nombre
        self.empresa = empresa


class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []

    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)


class Edificio:
    def __init__(self, nombre, ciudad, empresa):
        self.nombre = nombre
        self.ciudad = ciudad
        self.empresa = empresa



empresa_yoohoo = Empresa("YooHoo!")
ciudad_ny = Ciudad("New York")
ciudad_la = Ciudad("Los Angeles")

edificio_a = Edificio("A", ciudad_ny, empresa_yoohoo)
edificio_b = Edificio("B", ciudad_ny, empresa_yoohoo)
edificio_c = Edificio("C", ciudad_la, empresa_yoohoo)

empresa_yoohoo.agregar_edificio(edificio_a)
empresa_yoohoo.agregar_edificio(edificio_b)
empresa_yoohoo.agregar_edificio(edificio_c)

empleado_martin = Empleado("Sr. Martin", empresa_yoohoo)
empleado_salim = Empleado("Sr. Salim", empresa_yoohoo)
empleado_xing = Empleado("Sra. Xing", empresa_yoohoo)



empresa_yoohoo.edificios = [edificio_c]
ciudad_ny.edificios = []
