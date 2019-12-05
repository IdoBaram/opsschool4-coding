import json
from collections import defaultdict
import yaml

ppl_ages_group = defaultdict(list)
AGE = 1
LAST_ITEM = -1
NAME = 0

with open("hw.json", "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

border_min = 0
buckets = sorted(data["buckets"])
ppl_ages = sorted(data["ppl_ages"].items(), key=lambda kv: kv[AGE])
if ppl_ages[LAST_ITEM][AGE] >= buckets[LAST_ITEM]:
    border_max = ppl_ages[LAST_ITEM][AGE] + 1
else:
    border_max = buckets[LAST_ITEM]

for person in ppl_ages:
    if person[AGE] > buckets[LAST_ITEM]:
        border_min = buckets[LAST_ITEM]
        border_in_max = border_max
    else:
        for border in buckets:
            border_in_max = border
            if border_min <= person[AGE] < border_in_max:
                break
            else:
                border_min = border_in_max
                continue

    ppl_ages_group[f"{border_min}-{border_in_max}"].append(person[NAME])
print(yaml.dump(dict(ppl_ages_group), allow_unicode=True))


