# https://www.codewars.com/kata/525f277c7103571f47000147/train/python

from datetime import datetime


def get_start_time(schedules, duration):
    latter = ''
    former = ''
    
    # best_time = []
    # latter = ''
    # former = ''
    # for i in range(3):
    #     for person in schedules:
    #         for av_time in person:
    #             latter = av_time[0] if av_time[0] > latter else latter
    #             former = av_time[1] if av_time[1] > former else former
    #
    #             latter = datetime.strptime(latter, '%H:%M')
    #             former = datetime.strptime(former, '%H:%M')
    #
    #             subtracted_time = str(former - latter)
    #             time_obj = datetime.strptime(subtracted_time, '%H:%M:%S')
    #             minutes = (time_obj.hour * 60) + time_obj.minute
    #
    #             if minutes > duration:
    #                 return f'{latter.hour}:{latter.minute}'


availability = [
  [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
  [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
  [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
]


print(get_start_time(availability, 60))
