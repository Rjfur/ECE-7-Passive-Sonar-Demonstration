import sounddevice as sd
import soundfile as sf

class UserOutputStream(sd.OutputStream):
    """
    description to be created at a later time
    """
    def __init__(self):
        super().__init__()


    def callback(self):
        """
        called by stream periodically
        """
        pass

    def buttonToFile(self, index):
        if index == 1:
            # whale

            # try:
            #     fileObject = open("whale.wav", "r")
            #     data, fs = sf.read(fileObject)
            #     sd.play(data, fs)
            #     print("PLAYING whale.wav")
            # except Exception as e:
            #     print(e)

            # fileObject = open("whale.wav", "r")
            data, fs = sf.read("whale.wav")
            sd.play(data, fs)
            print("PLAYING whale.wav")

            # need to have some exception if it ends

        elif index == 2:
            # shrimp
            data, fs = sf.read("shrimp.wav")
            sd.play(data, fs)
            print("PLAYING shrimp.wav")
        elif index == 3:
            # shipping trawler
            data, fs = sf.read("boat.wav")
            sd.play(data, fs)
            print("PLAYING boat.wav")
        elif index == 4:
            # quiet target
            data, fs = sf.read("drone.wav")
            sd.play(data, fs)
            print("PLAYING drone.wav")
        elif index == 5:
            pass
        elif index == 6:
            pass
        elif index == 7:
            pass
        elif index == 8:
            pass
        else:
            pass

    def stopPlayback(self):
        sd.stop()

    # def buttonToFile(self, index):
    #     """
        
    #     """
    #     return {
    #         'a': 1,
    #         'b': 2
    #     }.get(x, 9)    # 9 is default if x not found