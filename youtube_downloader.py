import os
import subprocess

# Set your playlist URL here
playlist_url = "https://www.youtube.com/watch?v=5nyFfZnsyNY&list=PLcbfLm0DikmfcRWtJ2CkKLZZySMWc-cHx&index=4"

# Set output directory
output_dir = "yt_mp3_downloads"
os.makedirs(output_dir, exist_ok=True)

# yt-dlp command
command = [
    "yt-dlp",
    "--yes-playlist",                   # Download entire playlist
    "--extract-audio",                 # Extract audio only
    "--audio-format", "mp3",           # Convert to mp3
    "--audio-quality", "0",            # Best quality
    "-o", f"{output_dir}/%(title)s.%(ext)s",  # Output file naming
    playlist_url
]

# Run the command
subprocess.run(command)

print("âœ… Download complete!")
