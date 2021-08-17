import os
import pickle
from sklearn.naive_bayes import GaussianNB

# define the class encodings and reverse encodings
classes = {0: "Iris Setosa", 1: "Iris Versicolour", 2: "Iris Virginica"}
r_classes = {y: x for x, y in classes.items()}

# function to process data and return it in correct format
def process_data(data):
    processed = [
        {
            "age": d.age,
            "sex": d.sex,
            "bmi": d.bmi,
            "bp": d.bp,
            "tc": d.tc,
            "ldl": d.ldl,
            "hdl": d.hdl,
            "tch": d.tch,
            "tlg": d.tlg,
            "glu": d.glu,
            "diabetic_status": d.diabetic_status,
        }
        for d in data
    ]

    return processed
