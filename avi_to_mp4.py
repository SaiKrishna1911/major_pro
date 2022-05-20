import moviepy.editor as moviepy
clip = moviepy.VideoFileClip("AVIfiles/final_avi_video.avi")
clip.write_videofile("Enhanced_Video_files/EnhancedVideo.mp4")