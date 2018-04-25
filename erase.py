#!/usr/bin/python
import sys
import os
import pyprog
import click


def getSize(filename):
    st = os.path.getsize(filename) 
    return st


def main():

    if len(sys.argv) < 2 or any(map(lambda el: el == '--help', sys.argv[1:])): 
       print "Program shreds the file passed as first argument. If --delete is also defined, the file will be also get deleted"
       print "----------------------------------------------------------------------------------------------------------------" 
       print "Syntax: $ python erase.py <file-to-delete> --delete(optional) "
       return
    delete = any(map(lambda el: el == '--delete', sys.argv[1:]))
    if os.path.exists(sys.argv[1]):
       sbytes =  getSize(sys.argv[1])
       print "File path: "+os.path.realpath(sys.argv[1]) 
       print "File size: "+str(sbytes)+"bytes" 
       if delete:
         print "\033[31mMarked for DELETION\033[0m"
    else:
       print "The file doesn't exist! "
       return
    if not click.confirm('Do you want to continue?', default=False):    
      print "Quitting..."
      return    
    f = open(str(sys.argv[1]), 'rb+')
    print "-----------------------------------------------------------------"
    print "Beggin shreding..."
    prog = pyprog.ProgressBar(" ", "", sbytes)
    prog.update()

    for x in range(0, sbytes):
      f.seek(x)
      prog.set_stat(x + 1)
      prog.update()
      f.write(b"\x0a")
    
    f.close()
    if delete:
      print "\nMarked for deletion, deleting..."
      print "Finished"
      os.remove(sys.argv[1])
    else:
      print "\nFinished"
if __name__ == "__main__":
    main()
