from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class MediaPlayer(QMediaPlayer):
    """
    description to be created at a later time
    """
    def __init__(self):
        super().__init__()
        self.setVolume(50)  # initial volume, not muted

    def buttonToFile(self, index):
        if index == 1:
            # whale
            self.setMedia(QMediaContent(QUrl.fromLocalFile("./sounds/hump1.mp3")))
            # self.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/Jacob/Documents/repos/ECE-7-Passive-Sonar-Demonstration/sounds/hump1.mp3")))
            self.play()
            print("PLAYING whale sound")

        elif index == 2:
            # shrimp
            self.setMedia(QMediaContent(QUrl.fromLocalFile("./sounds/snap2.mp3")))
            self.play()
            print("PLAYING shrimp sound")
        elif index == 3:
            # ship
            self.setMedia(QMediaContent(QUrl.fromLocalFile("./sounds/light.mp3")))
            self.play()
            pass
        elif index == 4:
            # quiet target
            pass
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
        self.stop()


#region old_stuff
# class UserOutputStream(sd.OutputStream):
#     """
#     description to be created at a later time
#     """
#     def __init__(self):
#         super().__init__()

#     def buttonToFile(self, index):
#         if index == 1:
#             # whale

#             # try:
#             #     fileObject = open("whale.wav", "r")
#             #     data, fs = sf.read(fileObject)
#             #     sd.play(data, fs)
#             #     print("PLAYING whale.wav")
#             # except Exception as e:
#             #     print(e)

#             # fileObject = open("whale.wav", "r")
#             data, fs = sf.read("whale.wav")
#             sd.play(data, fs)
#             print("PLAYING whale.wav")

#             # need to have some exception if it ends

#         elif index == 2:
#             # shrimp
#             data, fs = sf.read("shrimp.wav")
#             sd.play(data, fs)
#             print("PLAYING shrimp.wav")
#         elif index == 3:
#             # shipping trawler
#             data, fs = sf.read("boat.wav")
#             sd.play(data, fs)
#             print("PLAYING boat.wav")
#         elif index == 4:
#             # quiet target
#             data, fs = sf.read("drone.wav")
#             sd.play(data, fs)
#             print("PLAYING drone.wav")
#         elif index == 5:
#             pass
#         elif index == 6:
#             pass
#         elif index == 7:
#             pass
#         elif index == 8:
#             pass
#         else:
#             pass

#     def stopPlayback(self):
#         sd.stop()

    # def buttonToFile(self, index):
    #     """
        
    #     """
    #     return {
    #         'a': 1,
    #         'b': 2
    #     }.get(x, 9)    # 9 is default if x not found

#endregion