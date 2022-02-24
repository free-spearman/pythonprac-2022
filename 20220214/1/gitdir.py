import zlib
import sys
from glob import iglob
from os.path import join

repo = sys.argv[1]
repopath = join(repo, "objects", "??", "*")
for objname in iglob(repopath):
    print(objname)
        
    with open(objname, "rb") as objfile:
        fullobj = zlib.decompress(objfile.read())
        header, _, body = fullobj.partition(b'\x00')
        objkind, size = header.split()
        print(objkind.decode(), int(size))
        if objkind == b'commit':
            print(body.decode())
        elif objkind == b'tree':
            while(body):
               treehdr, _, tail = body.partition(b'\x00')
               gitid, body = tail[:20], tail[20:]
               print(f'\t{treehdr.decode()} {gitid.hex()}')
