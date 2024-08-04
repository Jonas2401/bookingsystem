from datetime import datetime, timedelta

def get_free_slots(events, start_date, end_date):
    free_slots = []
    current_time = start_date
    while current_time < end_date:
        is_free = all(not (event.start_time <= current_time < event.end_time) for event in events)
        if is_free:
            free_slots.append(current_time)
        current_time += timedelta(minutes=30)
    return free_slots
