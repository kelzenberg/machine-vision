"""
Image Store
"""
from typing import Dict
from numpy import ndarray


class ImageStore:
    images: Dict[str, ndarray] = {}

    @classmethod
    def add(self, name: str, image: ndarray):
        print(f'(ImageStore.add) Add "{name}"')
        self.images.update({name: image})
        return self.get(name)

    @classmethod
    def get(self, name: str):
        return self.images.get(name)

    @classmethod
    def size(self):
        return len(self.images)
