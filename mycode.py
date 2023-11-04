import cv2

# Initialize the camera
camera = cv2.VideoCapture(0)  # Use 0 for the first camera, 1 for the second, and so on

# Check if the camera is opened successfully
if not camera.isOpened():
    print("Error: Could not open the camera")
else:
    # Capture a single frame from the camera
    ret, frame = camera.read()

    if ret:
        # Save the captured frame as an image in the current working directory
        cv2.imwrite("captured_image.jpg", frame)
        print("Image captured and saved as 'captured_image.jpg'")
    else:
        print("Error: Could not capture an image")

    # Release the camera
    camera.release()

# Close all OpenCV windows (if any are open)
cv2.destroyAllWindows()
