import cv2
from tkinter import Tk, messagebox

def turn_cam():
  """Attempts to open the camera and performs face detection. Displays an error message if camera access fails."""

  # Check camera access
  try:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
      raise Exception("Error accessing camera")
  except Exception as e:
    # Display error message using Tkinter
    root = Tk()
    root.withdraw()  # Hide the main Tkinter window
    messagebox.showerror("Camera Error", f"Failed to access camera: {str(e)}")
    return  # Exit the function if camera access fails

  # Load the pre-trained face detection classifier
  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

  while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    new_frame = cv2.flip(frame, 1)

    if not ret:
      break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
      cv2.rectangle(new_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with detected faces
    cv2.imshow('Face Detection', new_frame)

    # Exit the loop when the 'q' key is pressed
    key = cv2.waitKey(20)
    if key == 27:  # exit on ESC
      break

  # Release the camera and close the OpenCV window
  cap.release()
  cv2.destroyAllWindows()

# Call the function turn_cam()
