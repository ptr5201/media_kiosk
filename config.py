from pathlib import Path

MEDIA_ROOT = Path("/media/ptr5201/Extreme Pro")

PICTURES_ROOT = MEDIA_ROOT / "Pictures"
VIDEOS_ROOT = MEDIA_ROOT / "Videos"

HOST = "127.0.0.1"
PORT = 5001

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".heic",
}

VIDEO_EXTENSIONS = {
    ".mp4",
    ".3gp",
    ".3gpp",
    ".avi",
    ".mov",
}
