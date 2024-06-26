from pathlib import Path

path = Path()

FOLDERS = {
    "tmp": path.absolute() / "src" / "app" / "infra" / "tmp",
    "uploaded_images": path.absolute() / "src" / "ui" / "static" / "uploads" / "images",
}
