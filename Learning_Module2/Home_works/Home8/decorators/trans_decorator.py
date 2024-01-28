
class translate_decor:  # not done
    def __init__(self, func):
        self.function = func

    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)
        return result