import re
from test_training_sets import test_set, training_set


def extract(list):
    total = 0
    total_correct = 0
    for obj in list:
        total += 1
        poster = {"age":"", "gender":""}
        other = {"age":"", "gender":"", "relationship":""}
        m = re.findall("\[(.*?)\]", obj["title"])

        for counter, match in enumerate(m):
            age = re.findall(r'\d+', match)[0]
            uppercase = match.upper()
            gender = re.findall('M|F', uppercase)
            if (age):
                if (counter == 0):
                    poster["age"] = age
                else:
                    other["age"] = age
            if (gender):
                if (counter == 0):
                    poster["gender"] = gender[0]
                else:
                    other["gender"] = gender[0]
            
        if (obj["poster"] == poster and obj["other"]["gender"]  == other["gender"] and obj["other"]["age"] == other["age"]):
            total_correct += 1
        else:
            print "--------------------"
            print obj["title"]
            print "Correct: " + str(obj["poster"]) + " incorrect: " + str(poster)
            print "Correct: " + str(obj["other"]) + " incorrect: " + str(other)

    print str(total_correct) + " out of a possible " + str(total)

    
extract(test_set)
