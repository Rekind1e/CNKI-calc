import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default='inputs', help='input directory')
parser.add_argument('--output', type=str, default='output', help='output directory')
args = parser.parse_args()

cnt = set()

file_list = os.listdir(args.input)
with open(os.path.join(args.output, 'orgs.txt'), 'w', encoding='utf-8') as out:
  for filename in file_list:
    with open(os.path.join(args.input, filename), 'r', encoding='utf-8') as f:
      for line in f:
        _, _, _, orgs, *_ = line.split('&&')
        if not orgs: continue
        for org in orgs.split(';'):
          if org == 'Japan:':
            print(line)
          if org not in cnt:
            cnt.add(org)
            # out.write(f'{org}\n')