def create_event(name: str, day: str, time: str) -> dict:
    new_event = {"name": name, "day": day, "time": time}
    return new_event


schedule = []


def add_event(schedule: list[dict], event) -> dict:
    return schedule.append(event)


def find_by_day(schedule: list[dict], day: str) -> list[dict]:
    event_in_day = []
    for event in schedule:
        if event["day"] == day:
            event_in_day.append(event)
    return event_in_day


def remove_event(schedule: list[dict], name: str) -> list[dict]:
    for event in schedule:
        if event["name"] == name:
            schedule.remove(event)
    return schedule


def export_schedule(schedule: list[dict]):
    for item in schedule:
        print(f"{item['day']} {item['time']} - {item['name']}")

add_event(schedule, create_event("Physics", "Tue", "09:00"))
add_event(schedule, create_event("Math", "Mon", "09:00"))
add_event(schedule, create_event("Chemistry", "Tue", "09:00"))
export_schedule(schedule)

enter_name = input("Enter your name: ")
enter_day = input("Enter the day: ")
enter_time = input("Enter the time: ")
add_event(schedule, create_event(enter_name, enter_day, enter_time))

day_to_find = input("What day do you want to find?(Mon/Tue/Wed/Thur/Fri/Sat/Sun) ")
export_schedule(find_by_day(schedule, day_to_find))
# print(find_by_day(schedule, day_to_find))
# res = find_by_day(schedule, day_to_find)
# print(export_schedule(res))
