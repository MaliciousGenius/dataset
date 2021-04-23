#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas
import uuid

def  create_dataframe(name, text_files_dir):
    if os.path.exists(name + "/" + name + ".csv"):
        os.remove(name + "/" + name + ".csv")

    data = []

    for text_file in os.scandir(name + "/" + text_files_dir):
        if text_file.is_file() and text_file.path.split('.')[-1].lower() == 'summary':
            for line in open(text_file, 'r+').readlines():
                if line.find('—') > 0 and line[0].isupper():
                    data.append([text_file.name.split('.')[0], uuid.uuid4(), line])
 

    df = pandas.DataFrame(data, columns=["root_id", "result_id", "text"])

    df.to_csv(name + "/" + name + ".csv", index=False)
