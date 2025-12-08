logs = [('park', 12), ('river', 7), ('park', 5), ('mall', 3)]
finished = ['mall']
rides = {}
for name, count in logs:
    rides[name] = rides.get(name, 0) + count 
print(rides)
for finish in finished:
    delete = rides.pop(finish, "удален")
    print(f"{finished}: удален") 
print(rides)
