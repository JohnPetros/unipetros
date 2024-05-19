from werkzeug.datastructures import FileStorage
from uuid import uuid4 as generate_random_name

from core.constants.folders import FOLDERS
from infra.utils.file import File
from infra.providers.image_processor_provider import ImageProcessorProvider


class Avatar:
    def __init__(self, value, default_image_name="default-avatar.png"):
        self.value = value

        if default_image_name is not None:
            self.default_image_name = default_image_name

    def get_image_name(self):
        if isinstance(self.value, FileStorage):
            _, extension = self.value.filename.split(".")

            if self.default_image_name != "default-avatar.png":
                old_avatar_file = File(
                    FOLDERS["uploaded_images"], self.default_image_name
                )
                old_avatar_file.delete()

            image_name = f"{generate_random_name()}.{extension}"

            avatar_file = File(FOLDERS["uploaded_images"], image_name)

            self.value.save(avatar_file.path)

            image_processor = ImageProcessorProvider()
            image_processor.register(avatar_file.path)
            image_processor.resize(400, 400)
            image_processor.save()

            return image_name

        return self.default_image_name
