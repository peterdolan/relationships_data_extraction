# Potential improvements: stack rank relationships, take best one found (gf over so for example)
# spell check/simplifier (huband -> husband for example, daughter's -> daughter)
# delete "mid" from within captured parens
# compound words get dashed. "sister in law" -> "sister-in-law"

import re
from test_set import test_set
from training_set import training_set
from relationship_words import self_words, relation_words, male_relation_words, female_relation_words

def get_diff(correct, generated):
  if (correct["poster"] == generated["poster"] 
      and correct["counterpart"] == generated["counterpart"]):
    return 1
  else:
    print ("--------------------")
    print (correct["title"])
    if (correct["poster"]["gender"]  != generated["poster"]["gender"]):
      print ("Poster gender mismatch.  " + correct["poster"]["gender"] + "|" + generated["poster"]["gender"])
    if (correct["poster"]["age"]  != generated["poster"]["age"]):
      print ("Poster age mismatch.  " + correct["poster"]["age"] + "|" + generated["poster"]["age"])
    if (correct["counterpart"]["gender"]  != generated["counterpart"]["gender"]):
      print ("Counterpart gender mismatch.  " + correct["counterpart"]["gender"] + "|" + generated["counterpart"]["gender"])
    if (correct["counterpart"]["age"]  != generated["counterpart"]["age"]):
      print ("Counterpart age mismatch.  " + correct["counterpart"]["age"] + "|" + generated["counterpart"]["age"])
    if (correct["counterpart"]["relationship"]  != generated["counterpart"]["relationship"]):
      print ("Counterpart relationship mismatch.  " + correct["counterpart"]["relationship"] + "|" + generated["counterpart"]["relationship"])
    return 0

def create_poster_object(data):
    poster = {"age":"", "gender":""}

    age = re.findall(r'\d+', data[1])
    if (age and len(age) > 0):
      poster["age"] = age[0]

    gender = re.findall('M|F', data[1].upper())
    if (gender):
      poster["gender"] = gender[0]

    return poster

def create_counterpart_object(person, title):
  counterpart = {"age":"", "gender":"", "relationship":""}
  if (person[0].lower() in relation_words):
    counterpart["relationship"] = person[0].lower()

  age = re.findall(r'\d+', person[1])
  if (age and len(age) > 0):
    counterpart["age"] = age[0]

  gender = re.findall('M|F', person[1].upper())
  if (gender):
    counterpart["gender"] = gender[0]

  if not counterpart["relationship"]:
    for word in title.split(" "):
      if word in relation_words:
        counterpart["relationship"] = word
        break

  if counterpart["relationship"] in female_relation_words:
    counterpart["gender"] = "F"
  if counterpart["relationship"] in male_relation_words:
    counterpart["gender"] = "M"

  return counterpart 

def extract_relations(people, title):
  if (people[0][0].lower() in relation_words or people[1][0].lower() in self_words):
    poster = create_poster_object(people[1])
    counterpart = create_counterpart_object(people[0], title)
  else:
    poster = create_poster_object(people[0])
    counterpart = create_counterpart_object(people[1], title)
    
  return {"poster": poster, "counterpart": counterpart}
  
def extract(title):
  people = re.findall("(\w+)\s?(\[|\()(.*?)(\]|\))", title)
  if (len(people) == 2):
    for counter, match in enumerate(people):
      people[counter]  = match[0:4:2]
    relationships = extract_relations(people, title)
    relationships["title"] = title
    return relationships
  return ""


def extract_list(list):
  total = 0
  total_correct = 0
  for tagged_obj in list:
    relationships = extract(tagged_obj["title"])
    if (relationships != ""):
      total += 1
      total_correct += get_diff(tagged_obj, relationships)

  print (str(total_correct) + " out of a possible " + str(total))

#single = [{"title":"I [18 M] have been dating my gf [18 F] for a month, and I want to build our personal relationship more, rather than our physical relationship", "poster":{"age":"18", "gender":"M"}, "counterpart":{"age":"18", "gender":"F", "relationship":"gf"}}]
    
#extract_list(test_set)
