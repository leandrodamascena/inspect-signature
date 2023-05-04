from abc import ABC, abstractmethod


class BaseBuilder(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def builder(self, function):
        raise NotImplemented

    @abstractmethod
    def validate(self):
        raise NotImplemented

    @abstractmethod
    def flush(self):
        raise NotImplemented
