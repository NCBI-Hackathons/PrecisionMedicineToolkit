import sys
import glob
batch_list = sys.argv[1]
# List of IDs
batch_IDs = []
with open(batch_list) as F:
    for line in F:
        batch_IDs.append(line.strip())
IDs_found = []
for f in glob.glob("/base/Project_Space/sra/*"):
    split_string = f.split("/")
    ID = split_string[-1].split('.')[0]
    IDs_found.append(ID)
# Remove redundant
IDs_found = list(set(IDs_found))
count_missing = 0
for i in batch_IDs:
    if i not in IDs_found:
        print(i)
        count_missing += 1
print("\nIDs that are missing")
print(count_missing)
