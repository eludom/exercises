#! /usr/bin/env python

import myhash



animals = myhash.MyHash("dogs")
animals.set("foo","bar")
animals.set("foo","foo")

print "animal foo is ", animals.get("foo")
print "animal bar is ", animals.get("bar")



