class scanner:
    def __init__(self, id):
        self.known = False
        self.id = id
        self.x = 0
        self.y = 0
        self.z = 0
        self.beacons = []
    

scanners = []

with open('python/19.in','r') as f:
    for line in f.readlines():
        if line.startswith('---'):
            id = line.replace('--- scanner ','')
            id = id.replace(' ---', '')
            id = int(id)
            this_scanner = scanner(id)

        elif line == '\n':
            scanners.append(this_scanner)

        else:
            x, y, z = line.strip().split(',')
            this_scanner.beacons.append([int(x), int(y), int(z)])

for this_scanner in scanners:
    print()
    print(f'scanner: {this_scanner.id}')
    for beacon in this_scanner.beacons:
        print(beacon)