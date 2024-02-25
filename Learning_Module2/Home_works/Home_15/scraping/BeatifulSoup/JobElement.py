class JobElement:
    job_id=0
    logo = ""
    title = ""
    subtitle = ""
    location = ""
    date = ""

    def __init__(self, title, subtitle, location, date, job_id):
        self.date = date[0].text.strip()
        self.location = location[0].text.strip()
        self.subtitle = subtitle[0].text.strip()
        self.title = title[0].text.strip()
        self.job_id = job_id

    def __str__(self):
        return (f"JobElement(job_id={self.job_id}, "
                f"title={self.title}, subtitle={self.subtitle}, "
                f"location={self.location}, date={self.date})")
