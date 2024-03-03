from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, TRCK

# Open the MP3 file
audio = MP3(r"C:\Path\To\Your\File.mp3", ID3=ID3)

# Add ID3 tags
audio["TIT2"] = TIT2(encoding=3, text="Title")
audio["TPE1"] = TPE1(encoding=3, text="Album")
audio["TALB"] = TALB(encoding=3, text="Artist")
audio["TCON"] = TCON(encoding=3, text="Genre")
audio["TRCK"] = TRCK(encoding=3, text="1")

# Save the changes
audio.save()