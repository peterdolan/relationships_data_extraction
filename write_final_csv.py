import json
from title_extraction import extract

def json_readr(file):
    for line in open(file, mode="r"):
        yield json.loads(line)

f=open("final_relationship_data.csv", "a+")

def getRelationData():
    total = 0
    generator = json_readr('relationships')
    f.write("title,post_age,post_gen,count_age,count_gen,relationship,score,num_comments")
    for object in generator:
        relationships = extract(object["title"])
        print (relationships)
        if (total < 100000):
          total += 1
          if (relationships != ""):
            f.write(
                relationships["title"].replace(",", "") + "," +
                relationships["poster"]["age"] + "," +
                relationships["poster"]["gender"] + "," +
                relationships["counterpart"]["age"] + "," +
                relationships["counterpart"]["gender"] + "," +
                relationships["counterpart"]["relationship"] + "," +
                str(object["score"]) + "," +
                str(object["num_comments"]) + "\n")
        else:
          break
#total += 1
#f.write(object["title"].encode('utf-8') + '\n')

getRelationData()

