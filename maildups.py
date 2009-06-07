#!/usr/bin/python
import sys, shutils
import mailbox, hashlib

def main(args):
	if len(args) != 3:
		print "usage: %s <input file> <output file>" % args[0]

	shutils.copyfile(args[1], args[2])

	box = mailbox.mbox(args[2])
	hashes = {}
	for key in box.iterkeys():
		m = hashlib.md5()
		m.update(box.get_string(key))
		h = m.digest()

		if h not in hashes:
			hashes[h] = []
		hashes[h].append(key)
	
	for h, msglist in hashes.iteritems():
		for key in msglist[1:]:
			box.discard(key)

if __name__ = "__main__":
	main(sys.argv)
