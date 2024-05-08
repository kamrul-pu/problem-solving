import cv2
import os


def extract_frames_from_video(video_path, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the video file
    video_capture = cv2.VideoCapture(video_path)

    # Initialize frame count
    frame_count = 0

    # Read until video is completed
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        if not ret:
            break

        # Construct output file path
        output_file_path = os.path.join(output_dir, f"frame_{frame_count}.jpg")

        # Save the frame as an image file
        cv2.imwrite(output_file_path, frame)

        # Increment frame count
        frame_count += 1

    # Release the video capture object
    video_capture.release()

    print(f"Extracted {frame_count} frames from video '{video_path}' to '{output_dir}'")


# Example usage
input_video_path = "very_cute.flv"
output_directory = "vc_frames"

# Extract frames from the input video
extract_frames_from_video(input_video_path, output_directory)
