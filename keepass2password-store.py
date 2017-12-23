#!/usr/bin/python

import csv
import os
import sys
import gnupg


def main( kpfile):

    gpg = gnupg.GPG( homedir='~/.gnupg' )
    gpg.encoding = 'utf-8'

    key_list = gpg.list_keys()

    i = 0
    for key in key_list:
        print '  ' + str( i) + '  -  ' + str( key[ 'uids'][ 0 ] )
        i = i + 1

    key_num = int( raw_input( 'Which Key? ') )

    print key_num

    gpg_fingerprint = key_list[ key_num ][ 'fingerprint']


    csv_file = open( kpfile, 'r' )
    reader = csv.reader(csv_file, delimiter=',')
    reader.next()
    for row in reader:
        group = row[ 0]
        group = group[ 5: ]
        title = row[ 1]
        uname = row[ 2]
        pw = row[ 3]
        url = row[ 4]
        notes = row[ 5]
        fname = group + '/' + title

        buf = ''
        buf = buf + pw + '\n'
        buf = buf + 'Username: ' + uname + '\n'
        buf = buf + 'URL: ' + url + '\n'
        buf = buf + 'Notes:' + '\n'
        buf = buf + notes + '\n'

        if not os.path.exists(os.path.dirname(fname)):
            os.makedirs(os.path.dirname(fname) )

        bufe = gpg.encrypt( buf, gpg_fingerprint)

        outfil = open( fname + '.gpg', 'wb')
        outfil.write( bufe.data)
        outfil.close()

        sys.stdout.write( '.')
        sys.stdout.flush()

    print



if __name__ == '__main__':
    if len( sys.argv) > 1:
        main( sys.argv[1])
    else:
        print 'Usage: password-store2keepass.py KEEPASS-CSV-FILE'
