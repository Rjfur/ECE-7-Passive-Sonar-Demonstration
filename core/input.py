import sounddevice as sd
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

# For handling debug output
import logging

# For getting size of sample in bytes
import sys

class UserInputStream(sd.InputStream):
    """
    description to be created at a later time
    """
    def __init__(self, debug):
        # call sd.InputStream initialization
        # Try to open Virtual Audio Cable input device. If the Virtual Cable is not active, then initiate the
        # sounddevice input stream with default device
        try:
            super().__init__(samplerate=48000, device="Line 1 (Virtual Audio Cable), Windows WASAPI",
                             channels=2, dtype=np.int16, callback=self.inputCallback, latency="low")
        except ValueError:
            super().__init__(samplerate=48000, channels=2, dtype=np.int16, callback=self.inputCallback, latency="low")

        self.debug = debug

        # initialize values used for input callback
        self.currentTime = 0
        #self.timeDifference = 0
        self.time_x = np.linspace(0.0, 0.1, 480)

        self.l = np.linspace(0.0, 1.0, 480)
        self.r = np.linspace(0.0, 1.0, 480)

        self.fftL = []
        self.fftR = []

        # used for setting up plot
        self.fig = plt.figure()
        # self.ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
        self.ax = plt.axes()
        self.line, = self.ax.plot([], [], lw=3)

        # anim = FuncAnimation(self.fig, self.animateFrame, init_func=self.initPlot, interval=20, blit=True)

    def inputCallback(self, indata, frames, time, status):
        """
        called by stream periodically
        """
        # print("ADC time: ", time.inputBufferAdcTime)
        # print("current time: ", time.currentTime)
        # print("time difference: ", time.inputBufferAdcTime - time.currentTime)
        # print("{0:6} | {1:6}".format(indata[0][0], indata[0][1]))

        # print((time.currentTime - self.currentTime) * 1000)

        # print(self.latency)
        self.timeDifference = time.currentTime - self.currentTime
        self.currentTime = time.currentTime
        self.time_x = np.linspace(0.0, self.timeDifference, 480)

        self.l = [channel[0] for channel in indata]
        self.r = [channel[1] for channel in indata]

        self.fftL = np.fft.fft(self.l)
        self.fftR = np.fft.fft(self.r)

        if self.debug["samples"]:
            logging.info(indata.shape[0])
        if self.debug["amplitude"]:
            logging.info(indata)
        if self.debug["bytes"]:
            # logging.info(indata[0][0])
            logging.info(sys.getsizeof(indata[0][0]))   # type: numpy mdarray
        if self.debug["time_processing"]:
            logging.info("processing time: {0}".format(time.inputBufferAdcTime - time.currentTime))

        # print(len(l))
        # print(len(r))
        # print(len(time))
        # plt.plot(self.time_x, np.fft.fft(self.l))
        # plt.plot(time, r)
        # print(l)
        # print(indata[:][1])
        # plt.show()

    def initPlot(self):
        self.line.set_data([], [])
        return line,

    def animateFrame(self):
        self.line.set_data(self.time_x, self.l)
        return line,
        