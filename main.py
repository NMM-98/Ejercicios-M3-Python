if __name__ == "__main__":
    # ejercicio 1, m3.
    class Alumno():
        nombre = None
        nota = None

        def __init__(self, nombre, nota):
            self.nombre = nombre
            self.nota = nota
            print('el alumno se ha creado con éxito')

        def clasificacion(self):
            if self.nota >= 5:
                print('el alumno {} ha aprobado'.format(self.nombre))
            else:
                print('el alumno {} ha suspendido'.format(self.nombre))

        def __str__(self):
            return "la nota de {} es {}".format(self.nombre, self.nota)


    alumno1 = Alumno('Pedro', 6)
    alumno2 = Alumno('Eva', 5)
    alumno3 = Alumno('Octavio', 4)
    print(alumno1)
    print(alumno2)
    print(alumno3)
    alumno1.clasificacion()
    alumno2.clasificacion()
    alumno3.clasificacion()

# ejercicio 2, m3

if __name__ == "__main__":
    class Alumno():
        __nombre = None
        __nota = None

        def __init__(self, nombre, nota):
            self.__nombre = nombre
            self.__nota = nota
            print('el alumno se ha creado con éxito')

        @property
        def nombre(self):
            return self.__nombre

        @property
        def nota(self):
            return self.__nota

        @nombre.setter
        def nombre(self, nombre):
            self.__nombre = nombre

        @nota.setter
        def nota(self, nota):
            self.__nota = nota

        def clasificacion(self):
            if self.__nota >= 5:
                print('el alumno {} ha aprobado'.format(self.__nombre))
            else:
                print('el alumno {} ha suspendido'.format(self.__nombre))

        def __str__(self):
            return "la nota de {} es {}".format(self.__nombre, self.__nota)


    alumno1 = Alumno('Pedro', 6)
    alumno2 = Alumno('Eva', 5)
    alumno3 = Alumno('Octavio', 4)
    print(alumno1)
    print(alumno2)
    print(alumno3)
    alumno1.clasificacion()
    alumno2.clasificacion()
    alumno3.clasificacion()
    alumno1.nota = 10
    print(alumno1.nota)
    print(alumno1.nombre)


    # ejercicio 3, m3

    class Producto():
        __codigo = None
        __nombre = None
        __precio = None
        __tipo = None

        def __init__(self, codigo, nombre, precio, tipo):
            self.__codigo = codigo
            self.__nombre = nombre
            self.__precio = precio
            self.__tipo = tipo
            print('se ha creado el producto.')

        @property
        def codigo(self):
            return self.__codigo

        @codigo.setter
        def codigo(self, codigo):
            self.__codigo = codigo

        @property
        def nombre(self):
            return self.__nombre

        @nombre.setter
        def nombre(self, nombre):
            self.__nombre = nombre

        @property
        def precio(self):
            return self.__precio

        @precio.setter
        def precio(self, precio):
            self.__precio = precio

        @property
        def tipo(self):
            return self.__tipo

        @tipo.setter
        def tipo(self, tipo):
            self.__tipo = tipo

        def __str__(self):
            return "codigo {}, nombre {}, precio {}, tipo {}".format(self.__codigo, self.__nombre, self.__precio,
                                                                     self.__tipo)


    cacao = Producto(9384, 'cocoa', 2, 'galleta')
    print(cacao)
    cacao.codigo = 1345
    cacao.nombre = 'Cacao'
    cacao.precio = 4
    cacao.tipo = 'Chocolate'
    print(cacao)
    print(cacao.codigo)


    # ejercicio 4, m3

    class Producto():
        __codigo = None
        __nombre = None
        __precio = None
        __tipo = None

        def __init__(self, codigo, nombre, precio, tipo):
            self.__codigo = codigo
            self.__nombre = nombre
            self.__precio = precio
            self.__tipo = tipo
            print('se ha creado el producto.')

        @property
        def codigo(self):
            return self.__codigo

        @codigo.setter
        def codigo(self, codigo):
            self.__codigo = codigo

        @property
        def nombre(self):
            return self.__nombre

        @nombre.setter
        def nombre(self, nombre):
            self.__nombre = nombre

        @property
        def precio(self):
            return self.__precio

        @precio.setter
        def precio(self, precio):
            self.__precio = precio

        @property
        def tipo(self):
            return self.__tipo

        @tipo.setter
        def tipo(self, tipo):
            self.__tipo = tipo

        def calcular_total(self, cantidad):
            total = self.__precio * cantidad
            return total

        def __str__(self):
            return "\nProbando el print:\nProducto con código {}:\n    Nombre: {}\n    Precio: {}\n    Tipo: {}".format(
                self.__codigo, self.__nombre, self.__precio, self.__tipo)


    cacao = Producto(9384, 'cocoa', 2, 'galleta')
    print(cacao)
    cacao.codigo = 1345
    cacao.nombre = 'Cacao'
    cacao.precio = 4
    cacao.tipo = 'Chocolate'
    print(cacao)
    print(cacao.codigo)
    print(cacao.calcular_total(6))


    # ejercicio 5, m3

    class Producto():
        __codigo = None
        __nombre = None
        __precio = None
        __tipo = None

        def __init__(self, codigo, nombre, precio, tipo):
            self.__codigo = codigo
            self.__nombre = nombre
            self.__precio = precio
            self.__tipo = tipo
            print('se ha creado el producto.')

        @property
        def codigo(self):
            return self.__codigo

        @codigo.setter
        def codigo(self, codigo):
            self.__codigo = codigo

        @property
        def nombre(self):
            return self.__nombre

        @nombre.setter
        def nombre(self, nombre):
            self.__nombre = nombre

        @property
        def precio(self):
            return self.__precio

        @precio.setter
        def precio(self, precio):
            self.__precio = precio

        @property
        def tipo(self):
            return self.__tipo

        @tipo.setter
        def tipo(self, tipo):
            self.__tipo = tipo

        def calcular_total(self, cantidad):
            total = self.__precio * cantidad
            return total

        def __str__(self):
            return "\nProbando el print:\nProducto con código {}:\n    Nombre: {}\n    Precio: {}\n    Tipo: {}".format(
                self.__codigo, self.__nombre, self.__precio, self.__tipo)


    cacao = Producto(9384, 'cocoa', 2, 'galleta')
    print(cacao)
    cacao.codigo = 1345
    cacao.nombre = 'Cacao'
    cacao.precio = 4
    cacao.tipo = 'Chocolate'
    print(cacao)
    print(cacao.codigo)
    print(cacao.calcular_total(6))


    # ejercicio 6, m3

    class Vehiculo():
        # atributos privados de clase "__"

        __color = None
        __ruedas = None

        # constructor Clase Vehiculo.

        def __init__(self, color, ruedas):
            self.__color = color
            self.__ruedas = ruedas

        # Getters y setters "@property, variable.setter"

        @property
        def color(self):
            return self.__color

        @color.setter
        def color(self, color):
            self.__color = color

        @property
        def ruedas(self):
            return self.__ruedas

        @ruedas.setter
        def ruedas(self, ruedas):
            self.__ruedas = ruedas

        def __str__(self):
            return 'Este vehículo tiene: \nColor: {} \nRuedas: {}.'.format(self.__color, self.__ruedas)


    coche1 = Vehiculo('rojo', 'nuevas')
    print(coche1)


    class Coche(Vehiculo):
        # atributos privados de clase.
        __velocidad = None
        __Cilindrada = None

        # constructor de clase.
        def __init__(self, color, ruedas, velocidad, cilindrada):
            Vehiculo.__init__(self, color, ruedas)
            self.__velocidad = velocidad
            self.__cilindrada = cilindrada

        @property
        def velocidad(self):
            return self.__velocidad

        @velocidad.setter
        def velocidad(self, velocidad):
            self.__velocidad = velocidad

        @property
        def cilindrada(self):
            return self.__cilindrada

        @cilindrada.setter
        def cilindrada(self, cilindrada):
            self.__cilindrada = cilindrada

        def __str__(self):
            return Vehiculo.__str__(self) + "\nVelocidad: {}\nCilindrada: {}".format(self.__velocidad,
                                                                                     self.__cilindrada)


    cocheDiez = Coche('azul', 'viejas', 100, 1500)
    print(cocheDiez)


    # ejercicio 7, m3

    class Vehiculo():
        # atributos privados de clase "__"

        __color = None
        __ruedas = None

        # constructor Clase Vehiculo.

        def __init__(self, color, ruedas):
            self.__color = color
            self.__ruedas = ruedas

        # Getters y setters "@property, variable.setter"

        @property
        def color(self):
            return self.__color

        @color.setter
        def color(self, color):
            self.__color = color

        @property
        def ruedas(self):
            return self.__ruedas

        @ruedas.setter
        def ruedas(self, ruedas):
            self.__ruedas = ruedas

        def __str__(self):
            return 'Este vehículo tiene: \nColor: {} \nRuedas: {}.'.format(self.__color, self.__ruedas)


    class Coche(Vehiculo):
        # atributos privados de clase.
        __velocidad = None
        __Cilindrada = None

        # constructor de clase.
        def __init__(self, color, ruedas, velocidad, cilindrada):
            Vehiculo.__init__(self, color, ruedas)
            self.__velocidad = velocidad
            self.__cilindrada = cilindrada

        @property
        def velocidad(self):
            return self.__velocidad

        @velocidad.setter
        def velocidad(self, velocidad):
            self.__velocidad = velocidad

        @property
        def cilindrada(self):
            return self.__cilindrada

        @cilindrada.setter
        def cilindrada(self, cilindrada):
            self.__cilindrada = cilindrada

        def __str__(self):
            return Vehiculo.__str__(self) + "\nVelocidad: {}\nCilindrada: {}".format(self.__velocidad,
                                                                                     self.__cilindrada)


    class Camioneta(Coche):
        __carga = None

        def __init__(self, color, ruedas, velocidad, cilindrada, carga):
            Coche.__init__(self, color, ruedas, velocidad, cilindrada)
            self.__carga = carga

        @property
        def carga(self):
            return self.__carga

        @carga.setter
        def carga(self, carga):
            self.__carga = carga

        def __str__(self):
            return Coche.__str__(self) + "\nCarga: {}".format(self.__carga)


    camioneta1 = Camioneta('verdes', 'nuevas', 200, 1000, 150)
    print(camioneta1)


    class Bicicleta(Vehiculo):
        __tipo = None

        def __init__(self, color, ruedas, tipo):
            Vehiculo.__init__(self, color, ruedas)
            self.__tipo = tipo

        @property
        def tipo(self):
            return self.__tipo

        @tipo.setter
        def tipo(self, tipo):
            self.__tipo = tipo

        def __str__(self):
            return Vehiculo.__str__(self) + "\nTipo: {}".format(self.__tipo)


    bicicleta1 = Bicicleta('amarilla', 'nuevas', 'montaña')
    print(bicicleta1)


    class Motocicleta(Bicicleta):
        __velocidad = None
        __cilindrada = None

        def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
            Bicicleta.__init__(self, color, ruedas, tipo)
            self.__velocidad = velocidad
            self.__cilindrada = cilindrada

        @property
        def velocidad(self):
            return self.__velocidad

        @velocidad.setter
        def velocidad(self, velocidad):
            self.__velocidad = velocidad

        @property
        def cilindrada(self):
            return self.__cilindrada

        @cilindrada.setter
        def cilindrada(self, cilindrada):
            self.__cilindrada = cilindrada

        def __str__(self):
            return Bicicleta.__str__(self) + "\nVelocidad: {}\nCilindrada: {}".format(self.__velocidad,
                                                                                      self.__cilindrada)
    motocicleta1 = Motocicleta('granate', 'viejas','A',300, 2000)
    print(motocicleta1)
    lista = [motocicleta1, bicicleta1, coche1]
    print(lista)


