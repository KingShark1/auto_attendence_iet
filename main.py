import cv2
from models import face_cropper

def main():
  
  weight_path_file = "haarcascade_frontalface_default.xml"
  manas_file = "dataset/DE19169.mp4"
  arinjay_file = "dataset/DE19170.mp4"
  antriksh_file = "dataset/DE19171.mp4"

  face_cropper.display_face(weight_path_file, video_file_path=antriksh_file)
  # face_cropper.play_video(video_path_file)
if __name__ == '__main__':
  main()  