La herencia múltiple es una característica de la programación orientada a objetos en Python en la que una clase (conocida como clase "hija") hereda atributos y métodos de dos o más clases "padre" simultáneamente. En la práctica, esto significa que una única clase puede agrupar y acceder a las funcionalidades, características y comportamientos de varias clases distintas a la vez. Para implementarla, basta con colocar las clases padre deseadas separadas por comas dentro de los paréntesis al definir la nueva clase.

Usos que puedes darle a la herencia múltiple:
1. Reutilización eficiente de código: Al heredar de múltiples fuentes, evitas reinventar la rueda o duplicar el mismo código en distintas partes de tu programa, manteniendo tus sistemas más modulares.
2. Combinar comportamientos independientes (ortogonales): Te permite fusionar características de dominios completamente separados en un solo objeto. Por ejemplo, en un videojuego podrías tener una clase Guerrero (daño físico) y una clase Mago (hechizos), y usar herencia múltiple para crear un GuerreroMagico que tenga acceso a ambas habilidades. Otro ejemplo clásico es fusionar las propiedades mecánicas y eléctricas para simular un VehículoHíbrido.
3. Implementar el patrón "Mixin": Este es un uso profesional muy común, que consiste en crear pequeñas clases sin atributos propios (solo con métodos) que sirven únicamente para inyectar funcionalidades extra a otras clases. Por ejemplo, podrías crear un Mixin que convierta objetos a formato JSON o que añada la capacidad de enviar correos, y "mezclarlo" (heredarlo) en cualquier clase que lo necesite.
4. Inyección de dependencias y extensión de frameworks: La herencia múltiple (particularmente mediante clases Mixin) actúa como una forma de inyección de dependencias que te permite personalizar y extender código que no controlas directamente, como el de librerías de terceros. Un ejemplo clásico ocurre en el framework web Django, donde se usa para añadir comportamientos modulares a las vistas de una página web; por ejemplo, heredando simultáneamente de LoginRequiredMixin (para exigir que el usuario inicie sesión) y PermissionRequiredMixin (para exigir permisos específicos).
5. Desarrollo de Interfaces Gráficas de Usuario (GUI): Es muy útil para proporcionar capacidades interactivas avanzadas de manera modular, combinando la funcionalidad estándar de una interfaz con propiedades físicas. Por ejemplo, crear un DraggableButton (Botón arrastrable) que hereda el renderizado visual y los clics de una clase Button, y la lógica para capturar las coordenadas del ratón de una clase Draggable.
6. Simulación de sistemas complejos: Permite fusionar ramas tecnológicas o lógicas totalmente independientes en un único objeto que debe exhibir las propiedades de ambas arquitecturas. En una simulación de transporte, se puede crear un VehículoHíbrido que herede tanto de un VehículoEléctrico (gestión de baterías y motores) como de un VehículoGasolina (transmisión mecánica y combustible).
7. Diseño de Videojuegos (RPGs): Sirve para evitar la duplicación de código al crear personajes con características híbridas que acceden a múltiples árboles de habilidades. Un ejemplo es diseñar un GuerreroMágico que hereda el cálculo de daño físico de la clase Guerrero y la gestión de maná y conjuros de la clase Mago.

- Un ejemplo muy sencillo para entender su funcionamiento:
Aquí tienes un caso en donde una clase hereda las características de dos contextos distintos: el personal y el institucional.

# Definimos la primera clase padre
class Estudiante:
    def presentar_estudiante(self):
        print("Soy un estudiante.")

# Definimos la segunda clase padre
class Instituto:
    def presentar_instituto(self):
        print("Estudio en el Instituto de Leyes 112.")

# La clase hija hereda de AMBAS clases a la vez (herencia múltiple)
class Derecho(Estudiante, Instituto): 
    def presentar_carrera(self):
        print("Y mi carrera es Derecho.")

# Creamos un objeto de la clase hija
manuel = Derecho()

# 'manuel' tiene acceso a los métodos de sus tres clases:
manuel.presentar_estudiante()  # Método heredado de Estudiante
manuel.presentar_instituto()   # Método heredado de Instituto
manuel.presentar_carrera()     # Método propio de Derecho
Como puedes notar, aunque el objeto fue instanciado exclusivamente desde la clase Derecho, la herencia múltiple le autoriza a utilizar sin problema los métodos que provienen tanto de Estudiante como de Instituto.