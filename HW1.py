import json
import yaml
import urllib.request


json_source = urllib.request.urlopen("https://raw.githubusercontent.com/IdoBaram/opsschool4-coding/master/hw.json")
json_raw = json_source.read()
j = json.loads(json_raw .decode("utf-8"))

sorted_buckets = j["buckets"]
sorted_buckets.sort()
print(sorted_buckets)

ppl = j["ppl_ages"]

max_age = 0
for k, v in ppl.items():
    if v > max_age:
        max_age = v
        max_age += 1

bucket_groups = {}

for i, v in enumerate(sorted_buckets):
    if i == 0:
        bucket_groups[str(0) + "-" + str(sorted_buckets[i])] = [0, sorted_buckets[i]]
    elif i == len(sorted_buckets) - 1:
        bucket_groups[str(sorted_buckets[i]) + "-" + str(max_age)] = [sorted_buckets[i], max_age]
    else:
        bucket_groups[str(sorted_buckets[i - 1]) + "-" + str(sorted_buckets[i])] = [sorted_buckets[i - 1],
                                                                                    sorted_buckets[i]]


final_result = {}
for k, v in bucket_groups.items():
    final_result[k] = []

for n, p in ppl.items():
    for k, v in bucket_groups.items():
        if p >= v[0] and p < v[1]:
            final_result[k].append(n)

yaml_parse = yaml.dump(final_result)

print(yaml_parse)