import mp3play
import time

filename = r'C:\Documents and Settings\Michael\Desktop\music.mp3'
clip = mp3play.load(filename)

clip.play()

time.sleep(min(30, clip.seconds()))
clip.stop()