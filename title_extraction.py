import re
from test_training_sets import test_set, training_set
from relationship_words import self_words, relation_words 

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

    age = re.findall(r'\d+', data[1])[0]
    if (age):
      poster["age"] = age

    gender = re.findall('M|F', data[1].upper())
    if (gender):
      poster["gender"] = gender[0]

    return poster

def create_counterpart_object(person):
  counterpart = {"age":"", "gender":"", "relationship":""}
  if (person[0].lower() in relation_words):
    counterpart["relationship"] = person[0].lower()

  age = re.findall(r'\d+', person[1])[0]
  if (age):
    counterpart["age"] = age

  gender = re.findall('M|F', person[1].upper())
  if (gender):
    counterpart["gender"] = gender[0]

  return counterpart 

def extract_relations(people):
  if (people[0][0].lower() in relation_words or people[1][0].lower() in self_words):
    poster = create_poster_object(people[1])
    counterpart = create_counterpart_object(people[0])
  else:
    poster = create_poster_object(people[0])
    counterpart = create_counterpart_object(people[1])
    
  return {"poster": poster, "counterpart": counterpart}
  


def extract(list):
  total = 0
  total_correct = 0
  for tagged_obj in list:
    people = re.findall("(\w+)\s?(\[|\()(.*?)(\]|\))", tagged_obj["title"])
    relationships = {}

    if (len(people) == 2):
      total += 1
      for counter, match in enumerate(people):
        people[counter]  = match[0:4:2]

      relationships = extract_relations(people)
      total_correct += get_diff(tagged_obj, relationships)

  print (str(total_correct) + " out of a possible " + str(total))

#single = [{"title":"I [18 M] have been dating my gf [18 F] for a month, and I want to build our personal relationship more, rather than our physical relationship", "poster":{"age":"18", "gender":"M"}, "counterpart":{"age":"18", "gender":"F", "relationship":"gf"}}]
single = [{"title":"What does he (22m) mean when he says this to me (21f)", "poster":{"age":"21", "gender":"F"}, "counterpart":{"age":"22", "gender":"M", "relationship":""}}]
    
extract(training_set)
