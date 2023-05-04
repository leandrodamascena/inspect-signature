import functools
import inspect, json
from typing import Callable, Dict, Any, List
from builder_example.builder.base import BaseBuilder


class Builder(BaseBuilder):
    def __init__(self) -> None:
        self._data_inspect: List[Dict[str, Any]] = []
        super().__init__()

    def builder(self, function) -> Callable:
        def wrapper(*args, **kwargs):
            # inspect class
            self._inspect_decorator(function, args, kwargs)
            # call function
            return function(*args, **kwargs)

        return wrapper

    def validate(self):
        return super().validate()

    def flush(self):
        json_object = json.dumps(self._data_inspect, indent=4)

        print("Flushing to file")
        with open("build.json", "w") as outfile:
            outfile.write(json_object)

    def _inspect_decorator(self, func, args, kwargs):

        print(f"Building function {func.__name__}")

        data_inspect: dict = {}

        data_inspect["function_name"] = func.__name__

        annotations = func.__annotations__
        for key in annotations:
            try:
                data_inspect[key] = {
                    str(annotations[key]): str(inspect.signature(annotations[key]))
                }
            except ValueError:
                data_inspect[key] = {str(annotations[key]): "builtin"}

        # Storing in memory all functions decorated
        self._data_inspect.append(data_inspect)

        return self._data_inspect
