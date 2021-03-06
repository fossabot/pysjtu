import datetime
from typing import List

from pysjtu.model.base import Result, Results


class Exam(Result):
    """
    A model which describes an exam. Some fields may be empty.

    :param name: name of the course on which you are being examined.
    :type name: str
    :param location: the place where this exam is held.
    :type location: str
    :param seat: seat number
    :type seat: int
    :param course_id: course id of the course on which you are being examined.
    :type course_id: str
    :param course_name: course name of the course on which you are being examined.
    :type course_name: str
    :param class_name: class name of the class you are attending on the course which are being examined.
    :type class_name: str
    :param rebuild: whether this exam is a rebuild test.
    :type rebuild: bool
    :param credit: credits that the course provides.
    :type credit: float
    :param self_study: whether this course is a self study course.
    :type self_study: bool
    :param date: date of the exam
    :type date: datetime.date
    :param time: time range of the exam
    :type time: List[datetime.time]
    """
    name: str
    location: str
    seat: int
    course_id: str
    course_name: str
    class_name: str
    rebuild: bool
    credit: float
    self_study: bool
    date: datetime.date
    time: List[datetime.time]

    _members = ["name", "location", "seat", "course_id", "course_name", "class_name", "rebuild", "credit", "self_study",
                "date", "time"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        date_out = self.date.strftime("%Y-%m-%d")
        time_out = [time.strftime("%H:%M") for time in self.time]
        return f"<Exam \"{self.name}\" location={self.location} datetime={date_out}({time_out[0]}-{time_out[1]})>"


from pysjtu.schema.exam import ExamSchema


class Exams(Results[Exam]):
    """
    A list-like interface to Exam collections.
    An additional filter method has been added to make filter operations easier.
    """
    _schema = ExamSchema
    _result_model = Exam
