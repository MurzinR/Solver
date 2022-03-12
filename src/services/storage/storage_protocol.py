__all__ = [
    'StorageProtocol',
]


import abc
import typing
import uuid

from ...model.solution import Solution
from ...model.task import Task, TaskTrace


class StorageProtocol(typing.Protocol):

    @abc.abstractmethod
    async def save_task(self, task: Task):
        pass

    @abc.abstractmethod
    async def load_task(self, task_id: uuid.UUID) -> Task:
        pass

    @abc.abstractmethod
    async def save_solution(self, solution: Solution):
        pass

    @abc.abstractmethod
    async def load_solution(self, task_id: uuid.UUID) -> Solution:
        pass

    @abc.abstractmethod
    async def save_task_trace(self, task_trace: TaskTrace):
        pass

    @abc.abstractmethod
    async def load_last_task_trace(self, task_id: uuid.UUID) -> TaskTrace:
        pass
