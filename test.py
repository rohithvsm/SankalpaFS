#!/usr/bin/env python

#    Copyright (C) 2001  Jeff Epler  <jepler@unpythonic.dhs.org>
#    Copyright (C) 2006  Csaba Henk  <csaba.henk@creo.hu>
#
#    This program can be distributed under the terms of the GNU LGPL.
#    See the file COPYING.
#

from grpc.beta import implementations
import sankalpa_fs_pb2


_TIMEOUT_SECONDS = 30

def get_server_mtime(proto_path):
    # pdb.set_trace()
    mt = stub.get_mtime(proto_path, _TIMEOUT_SECONDS).mtime
    print '********************************Server_mtime in get server mt %s' % mt
    return mt


def main():

    print get_server_mtime(sankalpa_fs_pb2.Path(path="/start.txt"))

if __name__ == '__main__':
    main()
