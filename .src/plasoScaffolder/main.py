# -*- coding: utf-8 -*-
import argparse

def Main():
  parser = argparse.ArgumentParser()
  group = parser.add_mutually_exclusive_group()
  group.add_argument("-s","--sqlite", help="SQLite Plugin",action="store_true")
  group.add_argument("-t","--test", help="Another Plugin",action="store_true")

  parser.add_argument("-g","--guide",help="Plugin Creation Guide",action="store_true")
  args = parser.parse_args()

  if args.sqlite:
    print("sqlite")

  if args.guide:
    print("start the guide")

if __name__ == '__main__':
  Main()