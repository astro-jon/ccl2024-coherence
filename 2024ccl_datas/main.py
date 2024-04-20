import json

import pandas as pd

if __name__ == '__main__':
    reader = json.load(open("track3/track3_test.json", "r", encoding = "utf-8"))
    length_list, course_list, fine_list = [], [], []
    for article in reader:
        try:length_list.append(len(article["sent"]))
        except: length_list.append(len(article["text"]))
        # course_list.append(len(article["CourseGrainedErrorType"]))
        # fine_list.append(len(article["FineGrainedErrorType"]))
    infodf = pd.DataFrame({
        "length": length_list, # "course_num": course_list, "fine_num": fine_list
    })
    print(1)
