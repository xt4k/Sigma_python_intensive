from Learning_Module2.Home_works.Home8.main import get_result

class short_form:          # short day_name form
    def __init__(self, func):
        self.function = func

    def __call__(self, *args, **kwargs):

        print("decor_sh_f")

        result = self.function(*args, **kwargs)
        return get_result(result)