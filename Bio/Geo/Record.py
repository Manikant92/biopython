# Copyright 2001 by Katharine Lindner.  All rights reserved.
# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.

"""Martel based parser to read GEO formatted files.

This is a huge regular regular expression for GEO, built using
the 'regular expressiona on steroids' capabilities of Martel.

#http://www.ncbi.nlm.nih.gov/geo/


Notes:
Just so I remember -- the new end of line syntax is:
  New regexp syntax - \R
     \R    means "\n|\r\n?"
     [\R]  means "[\n\r]"

This helps us have endlines be consistent across platforms.

"""
# standard library
import string


from Bio.Seq import Seq
from Bio.Align.Generic import Alignment
import Bio.Alphabet



"""Hold GEO data in a straightforward format.

classes:
o Record - All of the information in an GEO record.
"""

class Record:
    """Hold GEO information in a format similar to the original record.

    The Record class is meant to make data easy to get to when you are
    just interested in looking at GEO data.

    Attributes:
    entity_type
    entity_id
    entity_attributes
    col_defs
    table_rows

    """
    def __init__(self):
        self.entity_type = ''
        self.entity_id = ''
        self.entity_attributes = {}
        self.col_defs = {}
        self.table_rows = []

    def __str__( self ):
        output = ''
        output = output + 'GEO Type: %s\n' % self.entity_type
        output = output + 'GEO Id: %s\n' % self.entity_id
        att_keys = self.entity_attributes.keys()
        att_keys.sort()
        for key in att_keys:
            contents = self.entity_attributes[ key ]
            if( type( contents ) == type( [] ) ):
                for item in contents:
                    try:
                        output = output + '%s: %s\n' % ( key, item[ :40 ] )
                        output = output + out_block( item[ 40: ] )
                    except:
                        pass
            elif( type( contents ) == type( '' ) ):
                output = output + '%s: %s\n' % ( key, contents[ :40 ] )
                output = output + out_block( contents[ 40: ] )
            else:
                print contents
                output = output + '%s: %s\n' % ( key, val[ :40 ] )
                output = output + out_block( val[ 40: ] )
        col_keys = self.col_defs.keys()
        col_keys.sort()
        output = output + 'Column Header Definitions\n'
        for key in col_keys:
            val = self.col_defs[ key ]
            output = output + '    %s: %s\n' % ( key, val[ :40 ] )
            output = output + out_block( val[ 40: ], '    ' )
        for row in self.table_rows:
            output = output + '%s: ' % self.table_rows.index( row )
            for col in row:
                output = output + '%s\t' % col
            output = output + '\n'
        return output

def out_block( text, prefix = '' ):
    output = ''
    for j in range( 0, len( text ), 80 ):
        output = output + '%s%s\n'  % ( prefix, text[ j: j + 80 ] )
    output = output + '\n'
    return output










