import sounddevice as sd
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

# For handling debug output
import logging

# For getting size of sample in bytes
import sys

# For measuring current time
import time as time_module

# local import of localization code
from core.localization import Localization

class UserInputStream(sd.InputStream):
    """
    description to be created at a later time
    """
    def __init__(self, sampleRate, debug):
        # call sd.InputStream initialization
        # Try to open Virtual Audio Cable input device. If the Virtual Cable is not active, then initiate the
        # sounddevice input stream with default device
        try:
            super().__init__(samplerate=sampleRate, device="Line 1 (Virtual Audio Cable), Windows WASAPI",
                             channels=2, dtype=np.int16, callback=self.inputCallback, latency="low")
        except ValueError:
            super().__init__(samplerate=sampleRate, channels=2, dtype=np.int16, callback=self.inputCallback, latency="low")

        self.localization = Localization(sampleRate)
        
        self.sampleRate = sampleRate
        self.debug = debug

        # initialize values used for input callback
        self.currentTime = 0
        #self.timeDifference = 0
        self.time_x = None
        self.numSamples = None
        # self.time_x = np.linspace(0.0, 0.1, 480)

        # initial amplitude values
        self.l = None
        self.r = None
        # self.l = np.linspace(0.0, 1.0, 480)
        # self.r = np.linspace(0.0, 1.0, 480)

        # self.fftL = []
        # self.fftR = []

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

        if self.debug["time_localization"]:
            start = time_module.time()

        self.numSamples = indata.shape[0]
        self.timeDifference = time.currentTime - self.currentTime
        self.currentTime = time.currentTime
        self.time_x = np.linspace(0.0, self.timeDifference, self.numSamples)

        self.l = [channel[0] for channel in indata]
        self.r = [channel[1] for channel in indata]

        # self.fftL = np.fft.fft(self.l)
        # self.fftR = np.fft.fft(self.r)

        if self.debug["samples"]:
            logging.info(indata.shape[0])
        if self.debug["amplitude"]:
            logging.info(indata)
        if self.debug["bytes"]:
            # logging.info(indata[0][0])
            logging.info(self.dtype)
            # logging.info(sys.getsizeof(indata[0][0]))   # type: numpy mdarray
        if self.debug["time_processing"]:
            logging.info("processing time: {0} ms".format((time.inputBufferAdcTime - time.currentTime) * 1000))

        ######### localization #########
        self.localization.runLocalization(self.l, self.r)   # results stored to self.localization instance

        if self.debug["time_localization"]:
            logging.info("processing + localization time: {0} ms".format((time.inputBufferAdcTime - time.currentTime + time_module.time() - start) * 1000))

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
        self.line.set_data(self.localization.theta, self.localization.x)
        return line,
        