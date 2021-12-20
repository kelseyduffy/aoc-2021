class scanner:
    def __init__(self):
        self.beacons = set()
        self.transformed_beacons = set() #transform list of beacons into (0,0,0) perspective with no rotation
    

def transform_location(beacon, x, y, z, rotation):

    # apply the rotation to the beacon
    rotated_beacon = rotate_beacon(beacon, rotation)

    # move it along the necessary x, y, and z shifts
    transformed_beacon = (rotated_beacon[0] + x, rotated_beacon[1] + y, rotated_beacon[2] + z)

    return transformed_beacon

def rotate_beacon(beacon, rotation_id):
    
    global rotations

    # grab the actual rotation matrix from the list of 24 possibilities
    rotation_matrix = rotations[rotation_id]

    # apply the rotation
    new_x = beacon[0] * rotation_matrix[0][0] + beacon[1] * rotation_matrix[0][1] + beacon[2] * rotation_matrix[0][2]
    new_y = beacon[0] * rotation_matrix[1][0] + beacon[1] * rotation_matrix[1][1] + beacon[2] * rotation_matrix[1][2]
    new_z = beacon[0] * rotation_matrix[2][0] + beacon[1] * rotation_matrix[2][1] + beacon[2] * rotation_matrix[2][2]
    
    return (new_x, new_y, new_z)

def try_match_scanners(known_scanner, unknown_scanner):

    # try each of the 24 rotation transformations 
    global rotations

    for rot in range(len(rotations)):

        # create a new temporary set of transformed beacons for that rotation
        temp_rotated_unmoved_beacons = { transform_location(beacon, 0, 0, 0, rot) for beacon in unknown_scanner.beacons }

        # try each beacon in the known set against each beacon in the unknown set to see if those two are the same beacon, making the two scanners match
        for known_beacon in known_scanner.transformed_beacons:
            for unknown_beacon in temp_rotated_unmoved_beacons:
                
                # find the necessary x, y, z of the unknown scanner such that these beacons are the same at that rotation
                temp_x = known_beacon[0] - unknown_beacon[0]
                temp_y = known_beacon[1] - unknown_beacon[1]
                temp_z = known_beacon[2] - unknown_beacon[2]

                # make a new set of beacon positions in real space
                temp_rotated_moved_beacons = { transform_location(beacon, temp_x, temp_y, temp_z, 0) for beacon in temp_rotated_unmoved_beacons }

                # find the overlap if this were the same beacon
                matched_beacons = temp_rotated_moved_beacons.intersection(known_scanner.transformed_beacons)
                
                # if there are 12, return this as the matched scanner set
                if len(matched_beacons) >= 12:
                    return True, temp_x, temp_y, temp_z, rot

                # otherwise these aren't the same beacon, move on to the next one                
    
    # if we get this far, these two scanners don't overlap with each other
    return False, 0, 0, 0, 0

def manhattan_distance(first_scanner_location, second_scanner_location):
    x = abs(first_scanner_location[0] - second_scanner_location[0])
    y = abs(first_scanner_location[1] - second_scanner_location[1])
    z = abs(first_scanner_location[2] - second_scanner_location[2])
    return x + y + z

scanners = []
rotations = [                   # (1,2,3) becomes:
    [[1,0,0],[0,1,0],[0,0,1]],          # (1,2,3)
    [[1,0,0],[0,0,1],[0,-1,0]],         # (1,3,-2)
    [[1,0,0],[0,-1,0],[0,0,-1]],        # (1,-2,-3)
    [[1,0,0],[0,0,-1],[0,1,0]],         # (1,-3,2)
    [[-1,0,0],[0,-1,0],[0,0,1]],        # (-1,-2,3)
    [[-1,0,0],[0,0,1],[0,1,0]],         # (-1,3,2)
    [[-1,0,0],[0,1,0],[0,0,-1]],        # (-1,2,-3)
    [[-1,0,0],[0,0,-1],[0,-1,0]],       # (-1,-3,-2)
    [[0,-1,0],[1,0,0],[0,0,1]],         # (-2,1,3)
    [[0,0,1],[1,0,0],[0,1,0]],          # (3,1,2)
    [[0,1,0],[1,0,0],[0,0,-1]],         # (2,1,-3)
    [[0,0,-1],[1,0,0],[0,-1,0]],        # (-3,1,-2)
    [[0,1,0],[-1,0,0],[0,0,1]],         # (2,-1,3)
    [[0,0,1],[-1,0,0],[0,-1,0]],        # (3,-1,-2)
    [[0,-1,0],[-1,0,0],[0,0,-1]],       # (-2,-1,-3)
    [[0,0,-1],[-1,0,0],[0,1,0]],        # (-3,-1,2)
    [[0,0,-1],[0,1,0],[1,0,0]],         # (-3,2,1)
    [[0,1,0],[0,0,1],[1,0,0]],          # (2,3,1)
    [[0,0,1],[0,-1,0],[1,0,0]],         # (3,-2,1)
    [[0,-1,0],[0,0,-1],[1,0,0]],        # (-2,-3,1)
    [[0,0,1],[0,1,0],[-1,0,0]],         # (3,2,-1)
    [[0,1,0],[0,0,-1],[-1,0,0]],        # (2,-3,-1)
    [[0,0,-1],[0,-1,0],[-1,0,0]],       # (-3,-2,-1)
    [[0,-1,0],[0,0,1],[-1,0,0]]         # (-2,3,-1)
]


with open('python/19.in','r') as f:
    for line in f.readlines():
        if line.startswith('---'):
            """ I dont think I need the id for any reason
            id = line.replace('--- scanner ','')
            id = id.replace(' ---', '')
            id = int(id)
            this_scanner = scanner(id)"""
            this_scanner = scanner()

        elif line == '\n':
            scanners.append(this_scanner)

        else:
            x, y, z = line.strip().split(',')
            this_scanner.beacons.add((int(x), int(y), int(z)))
scanners.append(this_scanner)

## part 1 ##

# the first scanner sets the perspective. it's facing +x, +y, +z and is at (0,0,0)
scanners[0].transformed_beacons = { beacon for beacon in scanners[0].beacons }

# the actual set of beacons is therefore seeded with the first scanner's known set of beacons
actual_beacons = { beacon for beacon in scanners[0].transformed_beacons }

# we know the first scanner      
known_scanner_ids = { 0 }   

# we don't know anything from 1 to end
unkonwn_scanner_ids = { i for i in range(1,len(scanners)) }   
                                        
# keep track of where the scanners are, starting with scanner 0
scanner_locations = set()
scanner_locations.add((0,0,0))

# repeat until all scanners are known
while len(unkonwn_scanner_ids) > 0:                                 
    starting_count = len(known_scanner_ids)

    # try to match each of the unknown scanners to each of the known scanners
    matched_ids_this_round = set()
    for unknown_scanner_id in unkonwn_scanner_ids:
        for known_scanner_id in known_scanner_ids:
            matched, x, y, z, rotation = try_match_scanners(scanners[known_scanner_id], scanners[unknown_scanner_id])
            if matched:
                
                # if they matched, record the id in the list for later swapping from unknown to known
                matched_ids_this_round.add(unknown_scanner_id)
                
                # store this scanner's set of beacons with their transformed location
                scanners[unknown_scanner_id].transformed_beacons = { transform_location(beacon, x, y, z, rotation) for beacon in scanners[unknown_scanner_id].beacons }

                # add these beaconds to the list of actual beacons
                actual_beacons.update(scanners[unknown_scanner_id].transformed_beacons)

                scanner_locations.add((x,y,z))

                # move to the next unknown scanner
                break

    # move all the matched id for this round from the unknown list to the known list
    print(f'ids matched this round: {matched_ids_this_round}')
    unkonwn_scanner_ids -= matched_ids_this_round
    known_scanner_ids.update(matched_ids_this_round)

    # confirm that something matched on this loop
    ending_count = len(known_scanner_ids)
    assert ending_count > starting_count, 'no scanner was matched on this round'

print(len(actual_beacons))

## part 2 ##

max_distance = 0

for first_scanner_location in scanner_locations:
    for second_scanner_location in scanner_locations:
        this_distance = manhattan_distance(first_scanner_location, second_scanner_location)
        max_distance = max(max_distance, this_distance)

print(max_distance)