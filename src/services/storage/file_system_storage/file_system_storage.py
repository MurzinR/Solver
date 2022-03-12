__all__ = [
    'FileSystemStorage',
]

import uuid

from ..storage_protocol import StorageProtocol
from ....model.solution import Solution
from ....model.task import Task, TaskTrace


class FileSystemStorage(StorageProtocol):

    async def save_task(self, task: Task):
        raise NotImplementedError

    async def load_task(self, task_id: uuid.UUID) -> Task:
        raise NotImplementedError

    async def save_solution(self, solution: Solution):
        raise NotImplementedError

    async def load_solution(self, task_id: uuid.UUID) -> Solution:
        raise NotImplementedError

    async def save_task_trace(self, task_trace: TaskTrace):
        raise NotImplementedError

    async def load_last_task_trace(self, task_id: uuid.UUID) -> TaskTrace:
        raise NotImplementedError
