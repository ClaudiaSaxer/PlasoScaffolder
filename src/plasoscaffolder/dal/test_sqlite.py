import sqlite3

def testit():
  print('start')
  conn = sqlite3.connect('twitter_ios.db')
  c = conn.curser()


if __name__ == '__main__':
  testit()
