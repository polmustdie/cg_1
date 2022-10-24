import numpy as np
import pylab
from matplotlib.widgets import Slider, Button, RadioButtons


phi = np.arange(0, 2 * np.pi, 0.01)
ro = 1 - np.cos(phi)
if __name__ == '__main__':

    def updateGraph():
        global slider_a
        global graph_axes
        a = slider_a.val
        x = a * ro * np.cos(phi)
        y = a * ro * np.sin(phi)
        graph_axes.clear()
        graph_axes.grid(True)
        graph_axes.set_xlim([-10,10])
        graph_axes.set_ylim([-6, 6])
        graph_axes.plot(x, y)
        pylab.draw()


def onChangeValue(value):
    updateGraph()


# Создадим окно с графиком
fig, graph_axes = pylab.subplots()
# Оставим снизу от графика место для виджетов
fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.4)

# Создание слайдера для задания a
axes_slider_a = pylab.axes([0.05, 0.25, 0.85, 0.04])
slider_a = Slider(axes_slider_a, label='a', valmin=0.1, valmax=10.0, valinit=1, valfmt='%1.2f')
slider_a.on_changed(onChangeValue)
updateGraph()
pylab.show()