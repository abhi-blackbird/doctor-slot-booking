from django.db.models.fields import DateTimeField
from djongo import models



Doctor_CHOICES = (
 ('Dr1', 'Doctor1'),
 ('Dr2', 'Doctor2'),
)

TIMESLOT_LIST = (
 (0, '09:00 – 09:30'),
 (1, '10:00 – 10:30'),
 (2, '11:00 – 11:30'),
 (3, '12:00 – 12:30'),
 (4, '13:00 – 13:30'),
 (5, '14:00 – 14:30'),
 (6, '15:00 – 15:30'),
 (7, '16:00 – 16:30'),
 (8, '17:00 – 17:30'),
)

class appointment(models.Model):
    name = models.CharField(max_length=50)
    Age =models.IntegerField()
    date = models.DateField(help_text="YYYY-MM-DD")    
    Doctor = models.CharField( choices=Doctor_CHOICES, max_length=3)
    timeslot = models.IntegerField(choices=TIMESLOT_LIST)


    def __str__(self):
        return self.name

    # @property
    # def time(self):
    #     return self.TIMESLOT_LIST[self.timeslot][1]        
   
