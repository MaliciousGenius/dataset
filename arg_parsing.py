#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse


def arg_parser():
    """ Разбор аргументов командной строки"""

    # Парсер верхнего уровня
    parser = argparse.ArgumentParser(prog = "Dataset", description = "Управление набором данных")
    subparsers = parser.add_subparsers(help = "Команды верхнего уровня", dest = "action")

    # Парсеры подуровней
    subparsers = add_init_parser(subparsers)
    subparsers = add_analyze_parser(subparsers)

    arguments = parser.parse_args()
    return(arguments)


def add_init_parser(parser):
    """ Подготавливает парсер инициализации набора данных """

    init_parser = parser.add_parser("init", help = "Инициализировать файлы наборов данных")
    init_parser.add_argument("-n", "--name", help = "Имя для набора данных", default = "dataset")
    init_parser.add_argument("-w", "--words", help = "Список слов", required = True)

    return(parser)

def add_analyze_parser(parser):
    """ Подготавливает парсер анализа набора данных """

    analyze_parser = parser.add_parser("analyze", help = "Анализ набора данных")
    analyze_parser.add_argument("-n", "--name", help = "Имя для набора данных", default = "dataset")

    return(parser)
