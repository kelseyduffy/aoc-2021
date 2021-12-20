class scanner:
    def __init__(self):
        self.known = False
        self.x = 0
        self.y = 0
        self.z = 0
        self.beacons = set()
        self.transformed_beacons = set() #transform list of beacons into (0,0,0) perspective with no rotation
    

def transform_location(beacon, x, y, z, rotation):

    # apply the rotation to the beacon
    rotated_beacon = rotate_beacon(beacon, rotation)

    transformed_beacon = (rotated_beacon[0] + x, rotated_beacon[1] + y, rotated_beacon[2] + z)

    return transformed_beacon

def rotate_beacon(beacon, rotation):
    
    global rotations

    rotation_matrix = rotations[rotation]

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

        # try each beacon in the known set against each beacon in the unknown set to see if those being the same make the two scanners match
        for known_beacon in known_scanner.transformed_beacons:
            for unknown_beacon in temp_rotated_unmoved_beacons:
                
                # find the necessary x, y, z of the unknown scanner such that these beacons are the same
                temp_x = known_beacon[0] - unknown_beacon[0]
                temp_y = known_beacon[1] - unknown_beacon[1]
                temp_z = known_beacon[2] - unknown_beacon[2]

                # make a new set of beacon positions in real space
                temp_rotated_moved_beacons = { transform_location(beacon, temp_x, temp_y, temp_z, 0) for beacon in temp_rotated_unmoved_beacons }

                # find the overlap if this were the same beacon
                matched_beacons = temp_rotated_moved_beacons.intersection(known_scanner.transformed_beacons)
                
                # if there aren't at least 12 matches, these aren't the same beacon
                if len(matched_beacons) < 12:
                    continue

                # check if any of the known beacons are missing from this scanner if it were to be in this place
                # do I have to do this? saving for later I guess
                somethings_missing = False
                # TODO: check if something is missing

                if somethings_missing:
                    continue

                # if there are 12 matches and nothing is missing, return this as the matched scanner set
                return True, temp_x, temp_y, temp_z, rot
    
    # if we get this far, nothing matched
    return False, 0, 0, 0, 0

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




with open('python/test.in','r') as f:
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

# the first scanner sets the perspective. it's facing +x, +y, +z and is at (0,0,0)
scanners[0].known = True
scanners[0].transformed_beacons = { beacon for beacon in scanners[0].beacons }

# the actual set of beacons is therefore seeded with the first scanner's known set of beacons
actual_beacons = { beacon for beacon in scanners[0].transformed_beacons }

unkonwn_scanner_ids = { i for i in range(1,len(scanners)) }         # we don't know anything from 1 to 39
known_scanner_ids = { 0 }                                           # we know the first scanner

while len(unkonwn_scanner_ids) > 0:                                 # repeat until all scanners are known
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