import datetime, secrets, string, time, json, sys, os

options = "add <date> <message>, list, del <id>"
path = os.path.dirname(os.path.realpath(__file__))

if not os.path.isfile(f"{path}/alerts.json"):
    with open(f"{path}/alerts.json", 'w') as f: json.dump({}, f, indent=4)
with open(f"{path}/alerts.json") as handle: alerts = json.loads(handle.read())

if len(sys.argv) == 1:
    print(options)
elif sys.argv[1] == "add":
    priority, repeat = 10, 0
    for index, param in enumerate(sys.argv):
        if param == "--date":
            timestamp = int(time.mktime(datetime.datetime.strptime(sys.argv[index +1], "%d.%m.%Y-%H:%M").timetuple()))
        if param == "--message":
            message = sys.argv[index +1]
        if param == "--priority":
            priority = int(sys.argv[index +1])
        if param == "--repeat":
            repeat = int(sys.argv[index +1])
    id = ''.join(secrets.choice(string.ascii_letters) for _ in range(6))
    alerts[id] = {"timestamp":timestamp,"message":message,"priority": priority,"repeat":repeat,"runs":0}
    with open(f"{path}/alerts.json", 'w') as f: json.dump(alerts, f, indent=4)
elif sys.argv[1] == "list":
    for id,details in alerts.items():
        print(id,details)
elif sys.argv[1] == "del":
    if not sys.argv[2] in alerts: exit(f"Can't find {sys.argv[2]}")
    del alerts[sys.argv[2]]
    with open(f"{path}/alerts.json", 'w') as f: json.dump(alerts, f, indent=4)