from flask import Flask, render_template

from config import (
    MEDIA_ROOT,
    PICTURES_ROOT,
    VIDEOS_ROOT,
    IMAGE_EXTENSIONS,
    VIDEO_EXTENSIONS,
)

app = Flask(__name__)


def count_media(directory, extensions):
    if not directory.is_dir():
        return 0

    count = 0

    for path in directory.rglob("*"):
        if path.is_file() and path.suffix.lower() in extensions:
            count += 1

    return count


@app.route("/")
def index():
    media_root_available = MEDIA_ROOT.is_dir()
    pictures_available = PICTURES_ROOT.is_dir()
    videos_available = VIDEOS_ROOT.is_dir()

    picture_count = (
        count_media(PICTURES_ROOT, IMAGE_EXTENSIONS)
        if pictures_available
        else 0
    )

    video_count = (
        count_media(VIDEOS_ROOT, VIDEO_EXTENSIONS)
        if videos_available
        else 0
    )

    return render_template(
        "index.html",
        media_root_available=media_root_available,
        pictures_available=pictures_available,
        videos_available=videos_available,
        picture_count=picture_count,
        video_count=video_count,
    )


@app.route("/health")
def health():
    return {
        "status": "ok",
        "media_root_available": MEDIA_ROOT.is_dir(),
        "pictures_available": PICTURES_ROOT.is_dir(),
        "videos_available": VIDEOS_ROOT.is_dir(),
    }


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
