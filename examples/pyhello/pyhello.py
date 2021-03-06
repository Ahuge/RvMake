from rv import rvtypes, commands

__version__ = 1.1


class PyHello(rvtypes.MinorMode):
    "A simple example that shows how to make shift-Z start/stop playback"

    def togglePlayback(self, event):
        if commands.isPlaying():
            commands.stop()
            print "stopped"
        else:
            commands.play()
            print "playing"

    def __init__(self):
        rvtypes.MinorMode.__init__(self)
        self.init("pyhello",
                  [("key-down--Z", self.togglePlayback, "Z key")],
                  None,
                  [("Tools",
                    [("PYHELLO", self.togglePlayback, "Z", None)])])


def createMode():
    "Required to initialize the module. RV will call this function to create your mode."
    return PyHello()
