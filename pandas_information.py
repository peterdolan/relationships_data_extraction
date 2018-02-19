import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(filepath_or_buffer="/Users/peterdolan/Engineering/reddit/relationship_data.csv")

def get_distribution():
  plt.figure()
  data["relationship"].hist(bins = 100, range=[0,100]).plot()
  plt.savefig("temp.png")

def get_gender_stats():
#print (data.groupby(["post_gen"]).agg(['mean', 'count']))
  print ("greater than 1: ")
#print(data.loc[(data["score"] > 1)].groupby(["post_gen"]).agg(["mean", "count"]))
  print(data.loc[(data["score"] > 1) & (data["score"] < 100)].groupby(["post_gen"]).agg(["mean", "count"]))

def get_relationship_distribution():
  print (data["relationship"].value_counts())

def get_correlation():
  corr = data["post_gen"].corr(data["score"])
  print ('hi')
  print (corr)

get_gender_stats()
