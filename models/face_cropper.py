import cv2

def play_video(video_file_path: str):
  '''
  Plays video file whose address is passed in as input
  '''
 # Create a VideoCapture object and read from input file
  # If the input is the camera, pass 0 instead of the video file name
  cap = cv2.VideoCapture(video_file_path)

  # Check if camera opened successfully
  if (cap.isOpened()== False): 
    print("Error opening video stream or file")

  # Read until video is completed
  while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

      # Display the resulting frame
      cv2.imshow('Frame',frame)

      # Press Q on keyboard to  exit
      if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    # Break the loop
    else: 
      break

  # When everything done, release the video capture object
  cap.release()

  # Closes all the frames
  cv2.destroyAllWindows()

def display_face(model_weights_path: str, video_file_path: str):
  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + model_weights_path)

  # Capture video from video file
  cap = cv2.VideoCapture(video_file_path)

  # Check if camera opened successfully
  if (cap.isOpened()== False): 
    print("Error opening video stream or file")

  while (cap.isOpened()):
    # Read the frame
    ret, frame = cap.read()

    if ret == True:
      # Convert to grayscale
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

      # Detect the faces
      faces = face_cascade.detectMultiScale(frame, 1.1, 4)

      # Draw rectangle around each face
      for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

      # Display
      cv2.imshow("Frame", frame)

      # Press Q on keyboard to  exit
      if cv2.waitKey(25) & 0xFF == ord('q'):
        break
      
    else:
      break
      
    
  cap.release()
  cv2.destroyAllWindows()