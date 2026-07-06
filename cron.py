import requests, time, json, sys, os

path = os.path.dirname(os.path.realpath(__file__))

if not os.path.isfile(f"{path}/alerts.json"): exit("alerts.json not found")
with open(f"{path}/alerts.json") as handle: alerts = json.loads(handle.read())
if not os.path.isfile(f"{path}/config.json"): exit("config.json not found")
with open(f"{path}/config.json") as handle: config = json.loads(handle.read())

current = time.time()
for id,details in list(alerts.items()):
    if current > details['timestamp']:
        print(f"Running {id}")
        try:
            payload = {"title": details['message'], "message": details['message'], "priority": details['priority']}
            req = requests.post(f"{config['gotifyInstance']}/message?token={config['gotifyToken']}", json=payload, timeout=10)
            details['runs'] = details['runs'] +1
            if req.status_code == 200 and details['runs'] > details['repeat']: 
                del alerts[id]
        except Exception as ex:
            print(f"Failed to push {id}, got error: {ex}")

with open(f"{path}/alerts.json", 'w') as f: json.dump(alerts, f, indent=4)