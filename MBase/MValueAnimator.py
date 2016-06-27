from MBase.MFinalValueReachedException import MFinalValueReachedException

class MValueAnimator:
    """
    A class to animate single integer or float values. It would also
    help in applying various mathematical functions to the progress
    of the animation.
    """
    def __init__(self, initial_value, final_value, duration, fps):
        """

        :param initial_value:
        :param final_value:
        :param duration:
        :param fps:
        """
        self.__initial_value = initial_value
        self.__final_value = final_value
        self.__current_value = self.__initial_value
        self.__duration = duration
        self.__fps = fps
        self.__step_value = ((self.__final_value - self.__initial_value) / self.__fps) * (1000 / self.__duration)

    def step(self):
        """
        This method will return the next step value each time it is
        called. It will throw the MFinalValueReachedException if the
        final value is already reached.

        See value_animator_demo for usage.
        :return:
        """
        if self.__step_value > 0:
            if self.__current_value < self.__final_value:
                self.__current_value += self.__step_value
                if self.__current_value > self.__final_value:
                    self.__current_value = self.__final_value
            else:
                raise MFinalValueReachedException('I\'ve reached my bounds man...')
        else:
            if self.__current_value > self.__final_value:
                self.__current_value += self.__step_value
                if self.__current_value < self.__final_value:
                    self.__current_value = self.__final_value
            else:
                raise MFinalValueReachedException('I\'ve reached my bounds man...')
        return self.__current_value

    def get_original_value(self):
        """ Returns the initial value """
        return self.__initial_value

    def get_final_value(self):
        """ Returns the value to be reached i.e. final value """
        return self.__final_value

    def get_current_value(self):
        """ Return the current value, that's pretty obvious """
        return self.__current_value


