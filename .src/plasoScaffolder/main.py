# -*- coding: utf-8 -*-
import argparse

def Main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-sqlite","--sqlite", help="SQLite Plugin",action="store_true")
  args = parser.parse_args()

  if args.sqlite:
    print("sqlite")

if __name__ == '__main__':
  Main()