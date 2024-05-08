# import cv2


# def extract_frames(video_path):
#     # Open the video file
#     video_capture = cv2.VideoCapture(video_path)

#     frames = []
#     success, frame = video_capture.read()

#     # Loop through the video and extract frames
#     while success:
#         frames.append(frame)
#         success, frame = video_capture.read()

#     video_capture.release()
#     return frames


# def enhance_frame(frame):
#     # Apply image enhancement (e.g., denoising, color correction, etc.)
#     # Example: perform bilateral filtering for denoising
#     enhanced_frame = cv2.bilateralFilter(frame, d=9, sigmaColor=75, sigmaSpace=75)
#     return enhanced_frame


# def create_video(frames, output_path, fps=30):
#     # Define the codec and create VideoWriter object
#     fourcc = cv2.VideoWriter_fourcc(
#         *"mp4v"
#     )  # Define the codec (e.g., 'XVID', 'MJPG', 'mp4v')
#     height, width, _ = frames[0].shape
#     video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

#     # Write each enhanced frame to the video
#     for frame in frames:
#         video_writer.write(frame)

#     # Release the VideoWriter object
#     video_writer.release()


# def process_video(input_video_path, output_video_path):
#     # Step 1: Extract frames from the input video
#     frames = extract_frames(input_video_path)

#     # Step 2: Enhance each frame
#     enhanced_frames = [enhance_frame(frame) for frame in frames]

#     # Step 3: Recreate the video with enhanced frames
#     create_video(enhanced_frames, output_video_path)


# # Example usage
# input_video_path = "Savita.mp4"
# output_video_path = "output_video.mp4"
# process_video(input_video_path, output_video_path)

import cv2


def enhance_video(
    input_video_path, output_video_path, scale_factor=1.0, denoise_strength=10
):
    # Open the input video file
    video_capture = cv2.VideoCapture(input_video_path)

    # Get video properties
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(
        *"mp4v"
    )  # Define the codec (e.g., 'XVID', 'MJPG', 'mp4v')
    video_writer = cv2.VideoWriter(
        output_video_path, fourcc, fps, (frame_width, frame_height)
    )

    # Process each frame in the input video
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Resize the frame (optional)
        if scale_factor != 1.0:
            frame = cv2.resize(frame, None, fx=scale_factor, fy=scale_factor)

        # Apply denoising (e.g., bilateral filtering)
        if denoise_strength > 0:
            frame = cv2.bilateralFilter(frame, d=9, sigmaColor=75, sigmaSpace=75)

        # Write the processed frame to the output video
        video_writer.write(frame)

    # Release video capture and writer objects
    video_capture.release()
    video_writer.release()


# Example usage
input_video_path = "very_cute.flv"
output_video_path = "enhanced_video.mp4"

# Enhance video quality (adjust parameters as needed)
enhance_video(
    input_video_path, output_video_path, scale_factor=1.0, denoise_strength=10
)


# import cv2
# import subprocess


# def enhance_video(
#     input_video_path, output_video_path, scale_factor=1.0, denoise_strength=10
# ):
#     # Extract audio from input video
#     audio_extract_cmd = f'ffmpeg -i "{input_video_path}" -vn -acodec copy audio.mp4'
#     subprocess.call(audio_extract_cmd, shell=True)

#     # Open the input video file
#     video_capture = cv2.VideoCapture(input_video_path)

#     # Get video properties
#     fps = video_capture.get(cv2.CAP_PROP_FPS)
#     frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
#     frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

#     # Define the codec and create VideoWriter object
#     fourcc = cv2.VideoWriter_fourcc(
#         *"mp4v"
#     )  # Define the codec (e.g., 'XVID', 'MJPG', 'mp4v')
#     video_writer = cv2.VideoWriter(
#         output_video_path, fourcc, fps, (frame_width, frame_height)
#     )

#     # Process each frame in the input video
#     while True:
#         ret, frame = video_capture.read()
#         if not ret:
#             break

#         # Resize the frame (optional)
#         if scale_factor != 1.0:
#             frame = cv2.resize(frame, None, fx=scale_factor, fy=scale_factor)

#         # Apply denoising (e.g., bilateral filtering)
#         if denoise_strength > 0:
#             frame = cv2.bilateralFilter(frame, d=9, sigmaColor=75, sigmaSpace=75)

#         # Write the processed frame to the output video
#         video_writer.write(frame)

#     # Release video capture and writer objects
#     video_capture.release()
#     video_writer.release()

#     # Add audio to the enhanced video
#     audio_add_cmd = f'ffmpeg -i "{output_video_path}" -i audio.mp4 -c copy -map 0:v:0 -map 1:a:0 -shortest final_video.mp4'
#     subprocess.call(audio_add_cmd, shell=True)

#     # Cleanup temporary files
#     subprocess.call("rm audio.mp4", shell=True)


# # Example usage
# input_video_path = "very_cute.flv"
# output_video_path = "vc.flv"

# # Enhance video quality (adjust parameters as needed)
# enhance_video(
#     input_video_path, output_video_path, scale_factor=1.0, denoise_strength=10
# )
