import json
import math
import csv

def add_segment(segment):
    transcript["data"].append(segment)

with open ('clox_config_test.txt', 'r') as config_file:
    configuration = json.load(config_file)
    start_time = int(configuration['start_time'])

with open ('clox_results.txt', 'r') as json_file:
    data1 = json.load(json_file)
    data = json.loads(data1)
    seg = data["AudioFileResults"][0]["SegmentResults"]
    seglen = len(seg)
    print("Total segments:", seglen)
    transcript = { "data":[]}
    for i in range (0, seglen):
        lexical = seg[i]["NBest"][0]["Lexical"]
        onset = round(seg[i]["Offset"]/10000000, 3)
        onset = onset + start_time/1000
        offset = round(seg[i]["Duration"]/10000000 + onset, 3)
        offset = offset + start_time/1000
        segment = {}
        segment["lexical"] = lexical
        segment["onset"] = onset
        segment["offset"] = offset
        add_segment(segment)

with open ('clox_results2.csv', mode='w') as csv_file:
    fieldnames = ['lexical', 'onset', 'offset']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range (0, seglen):
        writer.writerow(transcript['data'][i])
    print("Done")