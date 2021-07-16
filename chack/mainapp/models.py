from djongo import models


class Appointment(models.Model):
    

    class Meta:
        unique_together = ('doctor', 'date', 'timeslot')

    TIMESLOT_LIST = (
        (0, '10:00 – 10:30'),
        (1, '11:00 – 11:30'),
        (2, '12:00 – 12:30'),
        (3, '13:00 – 13:30'),
        (4, '15:00 – 15:30'),
        (5, '16:00 – 16:30'),
        (6, '17:00 – 17:30'),
        (7, '18:00 - 18:30'),
        (8, '19:00 - 19:30'),
        )

    doctor = models.ForeignKey('Doctor',on_delete = models.CASCADE)
    date = models.DateField(help_text="YYYY-MM-DD")
    timeslot = models.IntegerField(choices=TIMESLOT_LIST)
    patient_name = models.CharField(max_length=60)

    def __str__(self):
        return '{} {} {}. Patient: {}'.format(self.date, self.time, self.doctor, self.patient_name)

    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]


class Doctor(models.Model):
    """Stores info about doctor"""

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    specialty = models.CharField(max_length=20)

    def __str__(self):
        return '{} {}'.format(self.specialty, self.short_name)

    @property
    def short_name(self):
        return '{} {}.{}.'.format(self.last_name.title(), self.first_name[0].upper(), self.middle_name[0].upper())
