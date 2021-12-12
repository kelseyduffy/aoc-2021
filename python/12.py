import copy

def visit_cave(caves, current_cave, route, total_routes, has_small_double):
    
    for cave in caves[current_cave]:
        this_double_tracker = has_small_double
        entry_route = [x for x in route]
        
        if cave == 'end':
            total_routes += 1
            continue 

        elif cave == 'start':
            continue
        
        elif cave == cave.lower():
            if entry_route.count(cave) > 1:
                continue

            elif entry_route.count(cave) == 1 and this_double_tracker:
                continue

            elif entry_route.count(cave) == 1 and not this_double_tracker:
                this_double_tracker = True    

        entry_route.append(cave)
        total_routes = visit_cave(caves, cave, entry_route, total_routes, this_double_tracker)
    
    return total_routes

routes = []

with open('python/12.in','r') as f:
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
has_small_double = False

for cave in caves['start']:
    current_route = [x for x in route]
    current_route.append(cave)
    total_routes = visit_cave(caves, cave, current_route, total_routes, has_small_double)

print(total_routes)