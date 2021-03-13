import os
import argparse
import json
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default='hhi_sample.json', help='input file')
parser.add_argument('--output', type=str, default='output_sample.json', help='output file')
args = parser.parse_args()

with open(args.input, 'r', encoding='utf-8') as f:
  data = json.load(f)
  data = data['by year']
  counter = defaultdict(int)
  counter2 = defaultdict(list)
  for j, hhi in data.items():
    for k, v in hhi.items():
      counter[k] += 1
      counter2[k].append(v)
  
  out1 = {x : counter[x] for x in sorted(counter.keys())}
  out2 = {x : sorted(counter2[x])[len(counter2[x]) // 2]for x in sorted(counter2.keys())}
  with open(args.output, 'w', encoding='utf-8') as o:
    out = {
      "num": out1,
      "median": out2
    }
    json.dump(out, o, indent=4)

