import json
import os, sys
import pymongo
import datatime

client = pymongo.MongoClient()
db = client['recopimp']

join_dict = {}
for catador in db['carroceiros'].find():
    join_dict[catador["id"]] = catador

for tel_info in db['telephones'].find():
    del tel_info['_id']
    join_dict[tel_info['catador_id']].update(tel_info)

for addr_info in db['addresses'].find():
    del addr_info['_id']
    join_dict[addr_info['catador_id']].update(addr_info)

for geo_info in db['geolocations'].find():
    del geo_info['_id']
    join_dict[geo_info['catador_id']].update(geo_info)


filename = ''.join([
        'usereco-',
        datetime.datetime.now().strftime("%Y%m%d-%H%hM%mSs"),
        '.json'])

with open(filename, 'w') as fp
    json.dumps(join_dict, fp, indent=4)
