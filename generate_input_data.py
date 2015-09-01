# -*- coding: utf-8 -*-

import uuid
import random
from datetime import datetime, timedelta

REGISTRATORS = ("REG-RU", "NIC-RU", "GO-DADDY", "CCTLD")
ZONES = ("RU", "РФ")

def get_randon_date():
    start = datetime.now() 
    end = start + timedelta(days=365)
    return start + (end - start) * random.random()

def get_pair():
    date = get_randon_date()
    return (date.date(), (date + timedelta(days=365)).date())

def get_row(zone):
    start, end = get_pair()
    return "{0}.{1} {2} {3} {4}".format(str(uuid.uuid4()), zone, start, end, random.choice(REGISTRATORS))

if __name__ == "__main__":
    import sys
    try:
        zone, filename, count = sys.argv[1], sys.argv[2], int(sys.argv[3])
    except:
        zone, filename, count = ZONES[0], "ALL-{0}.txt".format(ZONES[0]), 1000
    print ("Generate", filename, "with", count, "domains...")
    with open(filename, "w") as f:
        i = 0
        while i < count:
            f.write(get_row(zone)+"\n")
            i += 1
    print ("Finished")
    
    
    