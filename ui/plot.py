# Matplotlib imports for graphs/plots
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np

from PyQt5.QtWidgets import QSizePolicy

# used for measuring time for debugging
import time

# For handling debug output
import logging

# from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
# from matplotlib.backends.backend_qt5agg import FigureCanvas, \
#                                     NavigationToolbar2QT as NavigationToolbar
# from matplotlib.figure import Figure

class PlotCanvas(FigureCanvas):
    def __init__(self, debug, parent=None, width=5, height=4, dpi=100):
        self.debug = debug
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        #self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plotSetup()

    def plotSetup(self):
        # data = [6 for i in range(25)]
        self.ax = self.figure.add_subplot(111, projection='polar')  # set polar projection
        self.ax.set_theta_zero_location('W', offset=90) # want 0 degrees at bottom of plot
        self.ax.set_xlabel("Angle (deg)")
        # self.ax.set_xticks(np.pi/180. * np.linspace(180,  -180, 8, endpoint=False))
        # self.ax = plt.axes(xlim=(0, 20000), ylim=(0, 100000))
        self.line, = self.ax.plot([], [], lw=2)
        # ax.plot(data, 'r-')
        # ax.set_title('PyQt Matplotlib Example')
        self.draw()

    def beginAnimation(self, stream):
        self.anim = FuncAnimation(self.fig, self.animateFrame, init_func=self.clearPlot, interval=20, fargs=(stream,))
        
        # plt.show()
        self.draw()

    def clearPlot(self):
        # creating an empty plot/frame 
	    self.line.set_data([], []) 
	    return self.line, 

    def animateFrame(self, frame, stream):
        # frame automatically passed to function
        # self.ax.plot(stream.time_x, stream.r)

        if self.debug["time_update"]:
            beginFrame = time.time()

        # x = stream.time_x
        # y1 = stream.l # limit to first 480 samples?
        # y2 = stream.r # limit to first 480 samples?

        theta = stream.localization.theta
        x = stream.localization.x

        # notice we are only calling set_data once, and bundling the y values into an array
        # self.line.set_data(x, np.array([y1, y2]))
        self.ax.clear()
        # self.ax.set_xticks([0, 1, 2])
        self.ax.set_xlabel("Angle (deg)")
        # self.ax.set_ylabel("Amplitude")
        self.ax.set_theta_zero_location('W', offset=90) # want 0 degrees at bottom of plot
        # self.ax.set_thetamin(90)
        # self.ax.set_thetamax(270)
        # self.ax.text(0, 0, "Angle = {stream.localization.thetaHat}", horizontalalignment='right', verticalalignment='top')
        self.ax.annotate(f"Max Angle = {stream.localization.thetaHat:.1f}", xy=(0, 1), xytext=(0, 0), va='top', xycoords='axes fraction', textcoords='offset points')
        self.ax.plot(theta, x)

        # print(theta)
        # print(x)


        # self.ax.plot(x, y1)
        # self.ax.plot(x, y2)

        if self.debug["time_update"]:
            logging.info(time.time() - beginFrame)

        return self.line,

    # def animateFFT(self, frame, stream):
    #     self.ax.clear()
    #     self.ax.set_xlim([0, 20000])
    #     self.ax.set_ylim([0, 100000])
    #     t = np.linspace(0, 48000, num=480)
    #     freq = np.fft.fftfreq(t.shape[-1])
    #     sp = np.fft.fft(stream.l)
    #     sp2 = np.fft.fft(stream.r)
    #     self.ax.plot(t, sp.real)
    #     self.ax.plot(t, sp2.real)