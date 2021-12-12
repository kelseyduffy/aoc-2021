import copy

def visit_cave(caves, current_cave, route, total_routes):
    
    for cave in caves[current_cave]:
        
        entry_route = [x for x in route]
        
        if cave == 'end':
            total_routes += 1
            continue 
        elif cave == 'start':
            continue
        elif cave in entry_route and cave == cave.lower():
            previous_visits = entry_route.count(cave)
            if previous_visits >= 2:
                continue
            
        entry_route.append(cave)
        total_routes = visit_cave(caves, cave, entry_route, total_routes)
    
    return total_routes

routes = []

with open('python/test.in','r') as f:
    for x in f.readlines():
        routes.append(x.strip())

## part 1 ##

caves = {}
caves['start'] = set()
caves['end'] = set()

for route in routes:
    these_caves = route.split('-')

    if these_caves[0] not in caves:
        caves[these_caves[0]] = set()
    caves[these_caves[0]].add(these_caves[1])

    if these_caves[1] not in caves:
        caves[these_caves[1]] = set()
    caves[these_caves[1]].add(these_caves[0])

route = []
route.append('start')

total_routes = 0

for cave in caves['start']:
    current_route = [x for x in route]
    current_route.append(cave)
    total_routes = visit_cave(caves, cave, current_route, total_routes)

print(total_routes)