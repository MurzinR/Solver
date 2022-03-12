import uuid

import pydantic

from .base import BaseModel


__all__ = [
    'Solution',
]


class Solution(BaseModel):
    id: uuid.UUID = pydantic.Field(..., title='Solution ID')
    task_id: uuid.UUID = pydantic.Field(..., title='Task ID')
