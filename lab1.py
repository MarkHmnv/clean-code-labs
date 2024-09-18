from abc import ABC, abstractmethod


# 1. Abstract Base Class for Storages
class Storage(ABC):
    @abstractmethod
    def upload_file(self, file_path: str, destination: str) -> None:
        pass

    @abstractmethod
    def download_file(self, file_name: str, destination: str) -> None:
        pass

    @abstractmethod
    def delete_file(self, file_name: str) -> None:
        pass


# 2. Concrete Storage Classes
class LocalDiskStorage(Storage):
    def upload_file(self, file_path: str, destination: str) -> None:
        pass

    def download_file(self, file_name: str, destination: str) -> None:
        pass

    def delete_file(self, file_name: str) -> None:
        pass


class AmazonS3Storage(Storage):
    def upload_file(self, file_path: str, destination: str) -> None:
        pass

    def download_file(self, file_name: str, destination: str) -> None:
        pass

    def delete_file(self, file_name: str) -> None:
        pass


# 3. Singleton Storage Manager
class StorageManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StorageManager, cls).__new__(cls)
            cls._instance.storage_classes = {
                'local': LocalDiskStorage,
                's3': AmazonS3Storage,
            }
        return cls._instance

    def get_storage(self, storage_type: str) -> Storage:
        storage_class = self.storage_classes.get(storage_type)
        if storage_class:
            return storage_class()
        else:
            raise ValueError(f"Storage type '{storage_type}' not supported.")

    def add_storage_class(self, storage_type: str, storage_class) -> None:
        self.storage_classes[storage_type] = storage_class


if __name__ == "__main__":
    storage_manager = StorageManager()
    s3 = storage_manager.get_storage('s3')
    s3.upload_file('file path', 'destination')

    local_storage = storage_manager.get_storage('local')
    local_storage.upload_file('file path', 'destination')
