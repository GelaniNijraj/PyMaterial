__author__ = "Samvid Mistry"

from abc import abstractmethod

from PySide.QtCore import Signal

from MComponents.MShape import MShape


class MTwoStateShape(MShape):
    """
    An abstract class representing any MShape which can have binary state, which is checked and unchecked.
    Examples of this can be a checkbox, switch or a radio button.
    """
    checkedChangeSignal = Signal()

    def __init__(self):
        MShape.__init__(self)
        self.__checked = False

    @property
    def checked(self) -> bool:
        return self.__checked

    @checked.setter
    def checked(self, checked: bool):
        self.__checked = checked

    def when_check_changes(self, slot):
        if slot is not None:
            self.__checkedChangeSignal.connect(slot)

    def disconnect_slot(self, slot):
        if slot is not None:
            self.__checkedChangeSignal.disconnect(slot)

    @abstractmethod
    def check(self) -> bool:
        """
        Implementations should properly indicate the change in the state of the widget in implementation.
        WARNING: Subclasses implementing this method should call through super to make sure that the slots
        connected to change signal get notified properly.
        """
        if self.__checked is True:
            return False

        self.__checked = True
        self.checkedChangeSignal.emit()
        return True

    @abstractmethod
    def uncheck(self) -> bool:
        """
        Implementations should properly indicate the change in the state of the widget in implementation.
        WARNING: Subclasses implementing this method should call through super to make sure that the slots
        connected to change signal get notified properly.
        """
        if self.__checked is False:
            return False

        self.__checked = False
        self.checkedChangeSignal.emit()
        return True
