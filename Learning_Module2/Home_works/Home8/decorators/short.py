from Learning_Module2.Home_works.Home8.main import short_week_day_names


class short_form:  # short day_name decorator
    def __init__(self, func):
        self.function = func

    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)
        return short_week_day_names(result)
