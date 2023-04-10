class Cristal:
    def __init__(self, superficie):
        self.superficie = superficie
    
    def obtener_superficie(self):
        return self.superficie

class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion
        self.superficie_acristalada = Cristal(0)
    
    def obtener_superficie(self):
        return self.superficie_acristalada.obtener_superficie()

class Ventana:
    def __init__(self, pared, superficie, proteccion):
        self.pared = pared
        self.proteccion = proteccion
        self.superficie_acristalada = Cristal(superficie)
    
    def obtener_superficie(self):
        if self.proteccion is None:
            raise Exception("Protección obligatoria")
        return self.superficie_acristalada.obtener_superficie()

class ParedCortina:
    def __init__(self, orientacion, superficie):
        self.orientacion = orientacion
        self.superficie_acristalada = Cristal(superficie)
    
    def obtener_superficie(self):
        return self.superficie_acristalada.obtener_superficie()

class Casa:
    def __init__(self, paredes):
        self.paredes = paredes
    
    def superficie_acristalada(self):
        total = 0
        for pared in self.paredes:
            if isinstance(pared, ParedCortina):
                total += pared.obtener_superficie()
            elif isinstance(pared, Pared):
                total += pared.obtener_superficie()
                for ventana in pared.ventanas:
                    total += ventana.obtener_superficie()
            else:
                raise TypeError("La pared debe ser de tipo Pared o ParedCortina")
        return total

# Instanciación de las paredes 
pared_norte = Pared("NORTE") 
pared_oeste = Pared("OESTE") 
pared_sur = ParedCortina("SUR", 2) 
pared_este = Pared("ESTE") 

# Instanciación de las ventanas 
ventana_norte = Ventana(pared_norte, 0.5, "Persiana") 
ventana_oeste = Ventana(pared_oeste, 1, "Estor") 
ventana_sur = Ventana(pared_sur, 2, "Cortina") 
ventana_este = Ventana(pared_este, 1, "Persiana") 

# Agregar ventanas a paredes 
pared_norte.ventanas = [ventana_norte] 
pared_oeste.ventanas = [ventana_oeste] 
pared_este.ventanas = [ventana_este] 

# Instanciación de la casa con las 4 paredes 
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 
print(casa.superficie_acristalada()) 
