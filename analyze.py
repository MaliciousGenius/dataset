#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import uuid
import csv

def  create_dataframe(name, text_files_dir):
    if os.path.exists(name + "/" + name + ".csv"):
        os.remove(name + "/" + name + ".csv")

    data = []

    for text_file in os.scandir(name + "/" + text_files_dir):
        if text_file.is_file() and text_file.path.split('.')[-1].lower() == 'summary':
            for line in open(text_file, 'r+').readlines():
                if line.find('—') > 0 and line[0].isupper():
                    data.append([text_file.name.split('.')[0], uuid.uuid4(), line])
    
    
    with open(name + "/" + name + ".csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for item in data:
            csv_writer.writerow([item])
