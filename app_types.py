from typing import Any, TypedDict


class PersonalData:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Education:
    def __init__(self, school: str, grade: float) -> None:
        self.school = school
        self.grade = grade


class FullData:
    def __init__(self, name: str, age: int, school: str, grade: float) -> None:
        self.name = name
        self.age = age
        self.school = school
        self.grade = grade
