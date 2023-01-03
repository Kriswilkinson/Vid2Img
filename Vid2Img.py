import cv2
import os

# Replace "input.mp4" with the path to your video file
video_file = "D:\AI\Projects\Vid2Frames\Inputs\Y2Mate.is - French TV show invited people with unusual laughs to sit next to each other-FWAb3qDJWic-480p-1654307329269.mp4"

# Open the video file
video = cv2.VideoCapture(video_file)

# Find the number of frames in the video
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Create a folder to save the images
if not os.path.exists("images"):
    os.makedirs("images")

# Extract one frame per second
for i in range(total_frames):
    # Read the next frame
    success, frame = video.read()

    # Stop if we have reached the end of the video
    if not success:
        break

    # Save the frame as an image
    cv2.imwrite("images/image_{}.jpg".format(i), frame)

    # Jump to the next frame
    video.set(cv2.CAP_PROP_POS_FRAMES, i+30)

# Release the video file
video.release()
