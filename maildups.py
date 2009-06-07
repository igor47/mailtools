#!/usr/bin/python
import sys, shutil
import mailbox, hashlib

def main(args):
	if len(args) != 3:
		print "usage: %s <input file> <output file>" % args[0]

	shutil.copyfile(args[1], args[2])

	box = mailbox.mbox(args[2])
	hashes = {}
	total = 0
	for key in box.iterkeys():
		total += 1
		m = hashlib.md5()
		m.update(box.get_string(key))
		h = m.digest()

		if h not in hashes:
			hashes[h] = []
		hashes[h].append(key)
	print "Parsed %s messages" % total

	box.lock()
	discarded = 0
	for h, msglist in hashes.iteritems():
		for key in msglist[1:]:
			discarded += 1
			box.discard(key)
	box.unlock()
	box.close()
	print "discarded %s messages" % discarded

if __name__ == "__main__":
	main(sys.argv)
