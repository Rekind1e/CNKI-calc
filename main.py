import os
import argparse
from collections import Counter, defaultdict
import json

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default='inputs', help='input directory')
parser.add_argument('--output', type=str, default='output_lda', help='output directory')
args = parser.parse_args()


def run(in_path, out_path, filename):
  with open(os.path.join(in_path, filename) + '.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    _id = None
    author_cnt, org_cnt = defaultdict(Counter), defaultdict(Counter)
    for line in lines:
      _, info, authors, orgs, *_ = line.split('&&')
      year = info[-9:-5]
      if _id is None:
        _id = info[:-9]
      for author in authors.split(';'):
        if author:
          author_cnt[year][author] += 1
      for org in orgs.split(';'):
        if org:
          org_cnt[year][org] += 1

  data = {
    "name": filename.split('_')[0],
    "id": _id,
    "data": {
      "authors": {},
      "orgs": {}
    }
  }
  data_by_year = {
    "name": filename.split('_')[0],
    "id": _id,
    "data": {
      "authors": {},
      "orgs": {}
    }
  }

  for year, d in author_cnt.items():
    data_by_year["data"]["authors"][year] = dict(d)
    for author, cnt in d.items():
      if author not in data["data"]["authors"]:
        data["data"]["authors"][author] = cnt
      data["data"]["authors"][author] += cnt
  for year, d in org_cnt.items():
    data_by_year["data"]["orgs"][year] = dict(d)
    for org, cnt in d.items():
      if org not in data["data"]["orgs"]:
        data["data"]["orgs"][org] = cnt
      data["data"]["orgs"][org] += cnt
  with open(os.path.join(out_path, filename) + '.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
  with open(os.path.join(out_path, filename) + '_by_year.json', 'w', encoding='utf-8') as f:
    json.dump(data_by_year, f, ensure_ascii=False, indent=4)
  


  
  

file_list = os.listdir(args.input)
for filename in file_list:
  run(args.input, args.output, os.path.splitext(filename)[0])


