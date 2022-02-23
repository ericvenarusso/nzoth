import yaml

from nzoth.utils.models.project import Project

class Config:

    @staticmethod
    def load(file_path: str) -> dict:
        with open(file_path) as stream:
            return Project(**yaml.safe_load(stream)).dict()
