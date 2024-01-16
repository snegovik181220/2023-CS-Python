from datetime import date, datetime, timezone
from typing import List


class Person:
    """
    >>> person = Person('Ivan', 'Ivanov', 'male', date(1999, 8, 12))
    >>> person
    Person('Ivan', 'Ivanov', 'male', datetime.date(1999, 8, 12))

    >>> Person('Ivan', 'Ivanov', 'male', datetime.now(tz=timezone.utc).date()).full_ages()
    0
    >>> Person('Ivan', 'Ivanov', 'man', "1989.4.26")
    Traceback (most recent call last):
        ...
    ValueError: bday must be date type
    """

    name: str
    surname: str
    sex: str
    bday: date

    def __init__(self, name: str, surname: str, sex: str, bday: date):
        self.name = name
        self.surname = surname
        self.sex = sex

        error_instance = "bday must be date type"
        if not isinstance(bday, date):
            raise ValueError(error_instance)

        self.bday = bday

    def __repr__(self) -> str:
        return f"Person({self.name!r}, {self.surname!r}, {self.sex!r}, {self.bday!r})"

    def __eq__(self, other: "Person") -> bool:
        return (
            self.name == other.name
            and self.surname == other.surname
            and self.sex == other.sex
            and self.bday == other.bday
        )

    def full_ages(self):
        today = datetime.now(tz=timezone.utc)
        return (
            today.year
            - self.bday.year
            - ((today.month, today.day) < (self.bday.month, self.bday.day))
        )


class Student(Person):
    """
    >>> student = Student('Ivan', 'Ivanov', 'male', date(1999, 8, 12), 161, 9)
    >>> student
    Student('Ivan', 'Ivanov', 'male', datetime.date(1999, 8, 12), 161, 9)
    """

    name: str
    surname: str
    sex: str
    bday: date
    group: int
    skill: int

    def __init__(self, name: str, surname: str, sex: str, bday: date, group: int, skill: int):
        super().__init__(name, surname, sex, bday)
        self.group = group
        self.skill = skill

    def __repr__(self) -> str:
        return (
            f"Student({self.name!r}, {self.surname!r}, {self.sex!r},"
            f" {self.bday!r}, {self.group!r}, {self.skill!r})"
        )

    def __eq__(self, other: "Student") -> bool:
        return (
            self.name == other.name
            and self.surname == other.surname
            and self.sex == other.sex
            and self.bday == other.bday
            and self.group == other.group
            and self.skill == other.skill
        )


class Group:
    """
    Encapsulates list of students
    """

    group: List[Student]

    def __init__(self, group: List[Student]):
        self.group = list(group)

    def __eq__(self, other: "Group") -> bool:
        return self.group == other.group

    def __repr__(self) -> str:
        return f"Group([{', '.join([repr(student) for student in self.group])}])"

    def sort_by_age(self, *, reverse: bool = False):
        self.group = sorted(self.group, key=lambda student: student.full_ages(), reverse=reverse)

    def sort_by_skill(self, *, reverse=False):
        self.group = sorted(self.group, key=lambda student: student.skill, reverse=reverse)

    def sort_by_age_and_skill(self, *, reverse=False):
        self.group = sorted(
            self.group, key=lambda student: (student.full_ages(), student.skill), reverse=reverse
        )
