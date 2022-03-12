import datetime
import enum
import uuid

import pydantic

from .base import BaseModel


__all__ = [
    'TaskStatus',
    'TaskTrace',
    'Task',
]


class TaskStatus(enum.Enum):
    CREATED = 'CREATED'
    SENT = 'SENT'
    SOLVING = 'SOLVING'
    SOLVED = 'SOLVED'
    FAILED = 'FAILED'


class TaskTrace(BaseModel):
    task_id: uuid.UUID = pydantic.Field(..., title='Task ID')
    recording_time: datetime.datetime = pydantic.Field(
        default_factory=datetime.datetime.now,
        title="Task trace's recording time",
    )
    task_status: TaskStatus = pydantic.Field(..., title='Task Status')
    user_message: str = pydantic.Field(..., title='Message for user')
    developer_message: str = pydantic.Field(..., title='Message for developer')


class Task(BaseModel):
    id: uuid.UUID = pydantic.Field(default_factory=uuid.uuid4, title='Task ID')
    sleep_time: datetime.timedelta = pydantic.Field(..., title='Task calculation time')
