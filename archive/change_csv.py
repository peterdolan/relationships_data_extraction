import csv

with open('titles_data.csv', 'rb') as csvfile:
  with open('test_set.py', 'w') as test:
    test.write("test_set = [")
    test_set = []
    reader = csv.reader(csvfile)
    for row in reader:
      new_obj = {}
      poster = {}
      counterpart = {}
      new_obj["title"] = row[0].strip()
      i = 0
      if len(row[1]) > 3:
        new_obj["title"] += row[1]
        i +=1
      if len(row[2]) > 3:
        new_obj["title"] += row[2]
        i +=1
      poster["age"] = row[1 + i].strip()
      poster["gender"] = row[2 + i].strip().upper()
      counterpart["age"] = row[3 + i].strip()
      counterpart["gender"] = row[4 + i].strip().upper()
      counterpart["relationship"] = row[5 + i].strip().lower()
      new_obj["poster"] = poster
      new_obj["counterpart"] = counterpart
      test_set.append(new_obj)
      test.write(str(new_obj).strip() + ',\n')
    test.write("]")
