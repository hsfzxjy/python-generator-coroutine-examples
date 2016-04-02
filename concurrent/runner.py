from event import events_list

def run():
    while len(events_list):
        for event in events_list:
            if event.is_ready():
                events_list.remove(event)
                break
