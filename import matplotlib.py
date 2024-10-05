import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Radios de los círculos
radius_circle1 = 5  # Radio del círculo amarillo
radius_circle2 = 5  # Radio del círculo azul

# Crear los círculos
circle1 = patches.Circle((10,10), radius_circle1, edgecolor='#fcffb5', facecolor='#fcffb5')  # Amarillo
circle2 = patches.Circle((10, 10), radius_circle2, edgecolor='blue', facecolor='blue')  # Azul

# Crear la barra horizontal
bar = plt.barh(0, 1, color='yellow')

# Configurar los límites de los ejes
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)

# Añadir el texto del porcentaje
percentage_text = ax.text(5, 0.2, '', ha='center', va='center', fontsize=12, color='black')

# Cálculo del área del círculo amarillo
area_circle1 = np.pi * radius_circle1**2  # Área del círculo amarillo

# Estado de arrastre
dragging = False

# Función para calcular el área de intersección entre dos círculos
def circle_intersection_area(d, r1, r2):
    """Calcula el área de intersección entre dos círculos con radios r1 y r2, separados por distancia d"""
    if d >= r1 + r2:
        return 0  # No hay intersección
    if d <= abs(r1 - r2):
        return np.pi * min(r1, r2)**2  # Un círculo está completamente dentro del otro
    
    # Fórmula para el área de intersección de dos círculos
    part1 = r1**2 * np.arccos((d**2 + r1**2 - r2**2) / (2 * d * r1))
    part2 = r2**2 * np.arccos((d**2 + r2**2 - r1**2) / (2 * d * r2))
    part3 = 0.5 * np.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
    
    return part1 + part2 - part3

# Función para actualizar el gráfico (barra y porcentaje)
def update_plot():
    # Calcular la distancia entre los centros del círculo azul y amarillo
    dist = np.sqrt((circle2.center[0] - circle1.center[0])**2 + (circle2.center[1] - circle1.center[1])**2)
    
    # Calcular el área de intersección entre los dos círculos
    area_intersection = circle_intersection_area(dist, radius_circle1, radius_circle2)
    
    # Calcular el porcentaje de área cubierta del círculo amarillo
    percentage = (area_intersection / area_circle1) * 100
    percentage = min(percentage, 100)  # Asegurar que el porcentaje no exceda el 100%
    
    # Actualizar el ancho de la barra según el porcentaje
    bar[0].set_width(percentage / 10)  # Ajustar el ancho de la barra al porcentaje
    
    # Actualizar el texto del porcentaje
    percentage_text.set_text(f'{percentage:.1f}%')
    percentage_text.set_x(percentage / 20)  # Colocar el texto sobre la barra

    fig.canvas.draw()

# Función que maneja el evento de clic del mouse
def on_click(event):
    global dragging
    # Verificar si el clic está dentro del círculo azul
    contains, _ = circle2.contains(event)
    if contains:
        dragging = True

# Función que maneja el evento de movimiento del mouse (arrastrar)
def on_motion(event):
    global dragging
    if dragging:
        # Actualizar la posición del círculo azul con el mouse
        circle2.center = (event.xdata, event.ydata)
        update_plot()

# Función que maneja el evento cuando se suelta el mouse
def on_release(event):
    global dragging
    dragging = False

# Conectar los eventos a la figura
fig.canvas.mpl_connect('button_press_event', on_click)
fig.canvas.mpl_connect('motion_notify_event', on_motion)
fig.canvas.mpl_connect('button_release_event', on_release)

# Añadir los círculos
ax.add_patch(circle1)
ax.add_patch(circle2)

# Eliminar el plano cartesiano
ax.axis('off')
ax.set_frame_on(False)

# Mantener la proporción de los ejes
plt.gca().set_aspect('equal', adjustable='box')

# Mostrar el gráfico
plt.show()
