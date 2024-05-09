from PIL import Image


class ImageProcessorProvider:
    def __init__(self) -> None:
        self.image = None
        self.image_path = None

    def register(self, image_path) -> None:
        self.image_path = image_path
        self.image = Image.open(image_path)

    def resize(self, width: int, height: int) -> None:
        if self.image is not None:
            self.image.thumbnail((width, height))

    def save(self) -> None:
        if self.image is not None and self.image_path is not None:
            self.image.save(self.image_path)
