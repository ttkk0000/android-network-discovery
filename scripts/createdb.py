#!/usr/bin/env python
import sqlite3
import os

db = 'oui.db'

try:
  os.remove(db)
except OSError, err:
  print err
conn = sqlite3.connect(db)
c = conn.cursor()
c.execute("create table oui (mac text, vendor text)")

i=0
for line in open("oui.txt"):
  if "base 16" in line:
    i+=1
    mac = line[:6]
    vendor = line[22:].replace("'", "`").strip()
    try:
      c.execute("insert into oui values ('%s', '%s')"%(mac, vendor))
    except sqlite3.OperationalError, err:
      print err 

print "%s records"%i

conn.commit()
c.close()
