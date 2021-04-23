#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wikipediaapi
import uuid


def get_page(word):
    wiki =  wikipediaapi.Wikipedia("ru")
    text = str()
    page =  wiki.page(word)
    if page.exists():
        return page
    else:
        return None

def save_item(path, text):
    with open(path + "/" + str(uuid.uuid4()) + ".summary", "w+") as out:
        out.write(text)
