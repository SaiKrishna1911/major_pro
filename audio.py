import moviepy.editor as mp
my_clip = mp.VideoFileClip("Inputfiles/opd.mp4")
my_clip.audio.write_audiofile("Audiofiles/audio.wav")