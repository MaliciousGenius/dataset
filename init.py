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

def save_item(path, page):
    uid = str(uuid.uuid4())

    with open(path + "/" + uid + ".summary", "w+") as out:
        out.write(page.summary)
        out.close()

    with open(path + "/" + uid + ".text", "w+") as out:
        out.write(page.text)
        out.close()
