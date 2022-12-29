"""
Image Store
"""

from typing import Dict
from numpy import ndarray


class ImageStore:
    images: Dict[str, ndarray] = {}

    @classmethod
    def getByName(self, name: str):
        return self.images.get(name)

    @classmethod
    def getByPosition(self, pos: int):
        return list(self.images.items())[pos]

    @classmethod
    def updateByName(self, name: str, image: ndarray):
        self.images.update({name: image})
        return self.getByName(name)

    @classmethod
    def size(self):
        return len(self.images)
