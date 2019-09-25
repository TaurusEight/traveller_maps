#!/usr/bin/env python3



import urllib.request
import urllib.parse

data = """
Kren          0108 B867882-7  M                 A  000 Po K4 VYYYY
Eurona        0203 D363256-3                       000    K4 VYYYY
Ceder         0204 FS00634-A                       000    K4 VYYYY
TENAVAR       0208 C664A70-3  S                    000    K4 VYYYY
Nurrim        0209 XA56672-2                    R  000    K4 VYYYY
Pluvia Cado   0303 C38A67B-5                       000    K4 VYYYY
CARTHAGE      0304 A821920-B  B                    000    K4 VYYYY
Envidien      0305 C577668-8                       000    K4 VYYYY
Seda          0308 C119431-9                       000    K4 VYYYY
Ruinil        0309 A6887C7-4                       000    K4 VYYYY
BARSALOW      0403 D8599DA-6                    A  000 In K4 VYYYY
Aequoris      0404 C21A543-7                       000    G3 VYYYY
Henderson     0408 G8C0337-A                       000    G3 VYYYY
Oculus        0504 B8387A3-9                       000    G3 VYYYY
Harrington    0505 C997740-9                       000    G3 VYYYY
Casaid        0507 F000888-9  M                    000 In G3 VYYYY
TUPREE        0508 C2209D9-7  M                 A  000 In G3 VYYYY
Hawkins       0601 D653640-4                       000    G3 VYYYY
Floral        0604 GS03322-9                       000    G3 VYYYY
Nema          0607 FS00660-A  B                    000    G3 VYYYY
Somnus        0608 C510ADA-9                    A  000    G3 VYYYY
Corador       0701 A751753-9                       000    G3 VYYYY
Marral        0702 G0007AA-8                       000    G3 VYYYY
FOREST        0707 F000A70-7  N                    000 In G3 VYYYY
Vandas        0708 A8B0855-A                       000    G3 VYYYY
Sominum Mons  0801 B977000-8                       000    G3 VYYYY
Toth          0806 E451731-1                       000    G3 VYYYY
Madeeha       0807 D651694-7                       000    G3 VYYYY
"""

data = data.replace( '\n', '' )
encoded = urllib.parse.urlencode( { 'psdata': data } )
url = 'http://zho.berka.com/data/random/subsector.ps?{}'.format( encoded )

with urllib.request.urlopen( url ) as F:
  ps =  F.read().decode( 'utf-8' )
ps = ps.replace( '(Ni)', '(  )' )
print( ps )
