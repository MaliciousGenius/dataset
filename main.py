#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from arg_parsing import arg_parser
from init import get_page, save_item
from analyze import create_dataframe

import os


text_files_dir = "text_files"


def main():
    """ Набор данных """

    args = arg_parser()

    if args.action == 'init':
        global text_files_dir

        try:
            os.mkdir(args.name)
            os.mkdir(args.name + "/" + (text_files_dir))
        except:
            print("Каталог набора данных уже существует")
        
        if len(args.words) > 0:
            for word in args.words.split(","):
                page = get_page(word)
                if page:
                    save_item(args.name + "/" + text_files_dir, page)
                else:
                    print("Слово \"" + word + "\" не определено")

    elif args.action == 'analyze':
        create_dataframe(args.name, text_files_dir)


if __name__ == '__main__':

    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nЗакрытие... Никаких изменений не сохранено!")
        pass
