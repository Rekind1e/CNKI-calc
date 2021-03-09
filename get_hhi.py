import os
import argparse
from collections import defaultdict
import json

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default='output_sample', help='input directory')
parser.add_argument('--output', type=str, default='hhi_sample.json', help='output file')
args = parser.parse_args()


def run(name, path):
  with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    cnt = data['data']['authors']
    total = sum(cnt.values())
    ans = 0
    for x in cnt.values():
      ans += (x / total) ** 2
  return ans

def run_by_year(name, path):
  ans = defaultdict(int)
  with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    for year, cnt in data["data"]["authors"].items():
      total = sum(cnt.values())
      for x in cnt.values():
        ans[year] += (x / total) ** 2
  return ans
        


file_list = os.listdir(args.input)
dic = {
  "naive": {},
  "by year" : {},
  "by area" : {}
}

with open(args.output, 'w', encoding='utf-8') as f:
  for filename in file_list:
    name, *suf = filename.split('_')
    if len(suf) > 1: 
      hhi = run_by_year(name, os.path.join(args.input, filename))
      dic["by year"][name] = dict(hhi)
    else:
      hhi = run(name, os.path.join(args.input, filename))
      dic["naive"][name] = hhi
  json.dump(dic, f, indent=4, ensure_ascii=False)


