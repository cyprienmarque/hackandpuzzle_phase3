import socket
import time
import math


class SpacialSound:
    """ class that holds the socket and the speakers positions"""
    def __init__(self, speakers: list, host = "192.168.7.2", port = 7562) -> None:
        """ speakers is a list of tuples (x,y)"""
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.SOL_UDP)
        self.host = host
        self.port = port
        self.speakers = speakers

    def fromXY(self,x,y, intensity):
        """ x,y are the coordinates of the sound source
            intensity is the intensity of the sound source
        """
        values = []
        for speaker in self.speakers:
            distance_sq = ((speaker[0]-x)**2 + (speaker[1]-y)**2)
            val = intensity/(1+distance_sq)
            #  clamp val between 0 and 255
            if val > 255:
                val = 255
            elif val < 0:
                val = 0
            values.append(int(val))
        self.s.sendto( bytes(values), (self.host, self.port))
        print(bytes(values))
        


if __name__ == "__main__":
    # create an objetc
    speakers = [(0,0),(1,0),(0,1),(1,1)]
    spacial_sound = SpacialSound(speakers)
    while True:
        for i in range(100):
            spacial_sound.fromXY(i/100,0, 255)
            time.sleep(0.2)