if  __name__ == "__main__":
    #ejercicio 1, m3.
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

#ejercicio 2, m3

if  __name__ == "__main__":
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

#ejercicio 3, m3

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
            return "codigo {}, nombre {}, precio {}, tipo {}".format(self.__codigo, self.__nombre, self.__precio, self.__tipo)


    cacao = Producto(9384, 'cocoa', 2, 'galleta')
    print(cacao)
    cacao.codigo = 1345
    cacao.nombre = 'Cacao'
    cacao.precio = 4
    cacao.tipo = 'Chocolate'
    print(cacao)
    print(cacao.codigo)

#ejercicio 4, m3