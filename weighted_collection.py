from typing import TypeVar, Generic, Dict, Optional, Type
import numpy as np


T = TypeVar("T")


class _WeightedObject:
    """
    An object with associated weighted probability.
    """

    def __init__(self, obj: T, weight: int):
        """
        :param obj: The object.
        :param weight: The probability weight.
        """

        self.obj = obj
        self.weight = weight

    def __hash__(self):
        return hash(self.obj)


class WeightedCollection(Generic[T]):
    """
    A collection of objects. The objects are chosen randomly, but the randomness is "weighted".
    For example: if "anakin" has a weight of 1, "constantine" a weight of 1, and "xenophon" a  weight of 2,
    then "xenophon" will be randomly selected 50% of the time, "anakin" 25% of the time, and "xenophon" 25% of the time.
    """

    def __init__(self, obj_type: Type[T], random_seed: int = 0):
        """
        :param obj_type: The type of objects that can be added to the collection.
        :param random_seed: The random number generator seed.
        """

        self._weight: int = 0
        self._objects: Dict[_WeightedObject, int] = {}
        self._rng = np.random.RandomState(random_seed)
        self.obj_type = obj_type

    def add(self, obj: T, weight: int) -> bool:
        """
        Add an object to the collection.

        :param obj: The object. Must not already be in the WeightedCollection.
        :param weight: The probability weight. Must be >0

        :return: True if the object was added.
        """

        if weight <= 0 or not isinstance(obj, self.obj_type):
            return False

        wo = _WeightedObject(obj, weight)
        if wo in self._objects:
            return False

        # Add to the total weight.
        self._weight += weight
        self._objects.update({wo: self._weight})
        return True

    def add_many(self, objs: Dict[T, int]) -> None:
        """
        Add many objects to the collection.

        :param objs: A dictionary of objects. Key = the object. Value = the probability weight (must be >0).
        """

        for obj in objs:
            self.add(obj, objs[obj])

    def remove(self, obj: T) -> bool:
        """
        Remove an object from the collection.

        :param obj: The object in the collection.

        :return: True if the object was removed.
        """

        temp: _WeightedObject = _WeightedObject(obj, -1)
        if temp not in self._objects:
            return False

        objects: Dict[_WeightedObject, int] = {}
        weight = 0
        for wo in self._objects:
            # Ignore this object.
            if wo.obj == obj:
                continue
            # Add all other objects.
            weight += wo.weight
            objects.update({wo: weight})
        self._objects = objects
        self._weight = weight
        return True

    def get(self) -> Optional[T]:
        """
        :return: A randomly selected object using the probability weights per object.
        """

        rnd = self._rng.randint(0, self._weight)
        for wo in self._objects:
            if self._objects[wo] > rnd:
                return wo.obj
        return None
