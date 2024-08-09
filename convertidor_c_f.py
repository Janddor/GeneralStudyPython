class ConvetidorTemperatura:
    MAX_CELSIUS = 100 # En mayus significa constante, es buena praxis
    MAX_FAHRENHEIT = 213 # En mayus significa constante, es buena praxis

    @classmethod
    def c_f(cls, celsius):
        if celsius > cls.MAX_CELSIUS:
            raise ValueError(f'Temperatura C demasiado alta: {celsius}')
        else:
            return celsius * (9/5) + 32

    @classmethod
    def f_c(cls, fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError(f'Temperatura F demasiado alta: {fahrenheit}')
        else:
            return (fahrenheit - 32) * (5/9)

if __name__ == '__main__':
    resultado = ConvetidorTemperatura.c_f(15)
    print(f'15 C a F: {resultado:.2f} Fahrenheit')

    resultado = ConvetidorTemperatura.f_c(10)
    print(f'10 F a C: {resultado:.2f} Celsius')