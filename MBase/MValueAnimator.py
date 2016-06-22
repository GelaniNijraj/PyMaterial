class MValueAnimator:
    def __init__(self, initial_value, final_value, duration, fps):
        self.__initial_value = initial_value
        self.__final_value = final_value
        self.__current_value = self.__initial_value
        self.__duration = duration
        self.__fps = fps
        self.__step_value = ((self.__final_value - self.__initial_value) / self.__fps) * (1000 / self.__duration)

    def step(self):
        if self.__step_value > 0:
            if self.__current_value < self.__final_value:
                self.__current_value += self.__step_value
                if self.__current_value > self.__final_value:
                    self.__current_value = self.__final_value
            else:
                raise OverflowError('I\'ve reached my bounds man...')
        else:
            if self.__current_value > self.__final_value:
                self.__current_value += self.__step_value
                if self.__current_value < self.__final_value:
                    self.__current_value = self.__final_value
            else:
                raise OverflowError('I\'ve reached my bounds man...')
        print("yeah", self.__current_value)
        return self.__current_value

    def get_original_value(self):
        return self.__initial_value

    def get_final_value(self):
        return self.__final_value

    def get_current_value(self):
        return self.__current_value