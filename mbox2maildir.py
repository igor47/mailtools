#!/usr/bin/python
import sys
import mailbox

def main(args):
	if len(args) != 3:
		print "usage: %s <mbox file> <maildir folde>" % args[0]
		print "the maildir folder will be created if it doesn't exist"

	inbox = mailbox.mbox(args[1], factory=None)
	outbox = mailbox.Maildir(args[2], factory=None, create=True)
	total = 0
	new = 0
	for msg in inbox:
		total += 1
		dirMsg = mailbox.MaildirMessage(msg)
		outbox.add(dirMsg)

	print "Parsed %s messages" % total

if __name__ == "__main__":
	main(sys.argv)
