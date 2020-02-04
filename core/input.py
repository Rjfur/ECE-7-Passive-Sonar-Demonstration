import sounddevice as sd
import numpy as np

class UserInputStream(sd.InputStream):
    """
    description to be created at a later time
    """
    def __init__(self):
        # call sd.InputStream initialization
        super().__init__(samplerate=48000, device="Line 1 (Virtual Audio Cable), Windows WASAPI",
                        channels=2, dtype=np.int16, callback=self.inputCallback)
        # initial setup
        # self.samplerate = 44100
        # self.device = "Mic 1 (Virtual Cable 1), Windows WDM-KS" # kernel streaming
        # self.dtype = np.int16
        # self.latency = "low"    # ???
        # self.callback = self.inputCallback

    def inputCallback(self, indata, frames, time, status):
        """
        called by stream periodically
        """
        # print("ADC time: ", time.inputBufferAdcTime)
        # print("current time: ", time.currentTime)
        # print("time difference: ", time.inputBufferAdcTime - time.currentTime)
        # print("{0:6} | {1:6}".format(indata[0][0], indata[0][1]))