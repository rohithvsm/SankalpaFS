#!/usr/bin/env python

#    Copyright (C) 2001  Jeff Epler  <jepler@unpythonic.dhs.org>
#    Copyright (C) 2006  Csaba Henk  <csaba.henk@creo.hu>
#
#    This program can be distributed under the terms of the GNU LGPL.
#    See the file COPYING.
#

from grpc.beta import implementations
import errno
import sankalpa_fs_pb2

import os, sys
from errno import *
from stat import *
import fcntl
# pull in some spaghetti to make this stuff work without fuse-py being installed
import tempfile

try:
    import _find_fuse_parts
except ImportError:
    pass
import fuse
from fuse import Fuse

stub = None
mount_point = None
root = None

_stream_packet_size = 64 * 1024  # TCP packet size
_stream_packet_size -= 60  # maximum TCP header size
_stream_packet_size -= 192  # maximum IPv4 header size
_stream_packet_size -= 24  # Ethernet header size

_TIMEOUT_SECONDS = 30

if not hasattr(fuse, '__version__'):
    raise RuntimeError, \
        "your fuse-py doesn't know of fuse.__version__, probably it's too old."

fuse.fuse_python_api = (0, 2)

fuse.feature_assert('stateful_files', 'has_init')


def flag2mode(flags):
    md = {os.O_RDONLY: 'r', os.O_WRONLY: 'w', os.O_RDWR: 'w+'}
    m = md[flags & (os.O_RDONLY | os.O_WRONLY | os.O_RDWR)]

    if flags | os.O_APPEND:
        m = m.replace('w', 'a', 1)

    return m

def _full_path(base_path, relative_path):
    if relative_path.startswith('/'):
        relative_path = relative_path[1:]
    return os.path.join(base_path, relative_path)


class Xmp(Fuse):

    def __init__(self, *args, **kw):

        Fuse.__init__(self, *args, **kw)

        # do stuff to set up your filesystem here, if you want
        #import thread
        #thread.start_new_thread(self.mythread, ())
        self.root = '/'

#    def mythread(self):
#
#        """
#        The beauty of the FUSE python implementation is that with the python interp
#        running in foreground, you can have threads
#        """
#        print "mythread: started"
#        while 1:
#            time.sleep(120)
#            print "mythread: ticking"

    def getattr(self, path):
        print '****************************************** getattr'
        stat = stub.getattr(sankalpa_fs_pb2.Path(path=path), _TIMEOUT_SECONDS)
        print '****************************************** server_stat.st_size %s' % stat.st_size
        return (stat.st_mode, stat.st_ino, stat.st_dev, stat.st_nlink, stat.st_uid, stat.st_gid,
                                                        stat.st_size, stat.st_atime, stat.st_mtime, stat.st_ctime)
        #return (getattr(stat, key)) for key in ('st_mode','st_ino','st_dev','st_nlink','st_uid','st_gid',
                                                        # 'st_size','st_atime','st_mtime','st_ctime'))
        # return os.lstat("." + path)
        # 'st_dev','st_ino',

    def readlink(self, path):
        return os.readlink("." + path)

    def readdir(self, path, offset):
        print '****************************************** readdir'

        for e in stub.readdir(sankalpa_fs_pb2.Path(path=path), _TIMEOUT_SECONDS).dir:
            print '****************************************** direntry %s' % e
            yield fuse.Direntry(e)
        # for e in os.listdir("." + path):
        #     yield fuse.Direntry(e)

    def unlink(self, path):
        print '****************************************** unlink'
        try:
            os.unlink("." + path)
        except OSError:
            pass
        return stub.delete(sankalpa_fs_pb2.Path(path=path), _TIMEOUT_SECONDS).status


    def rmdir(self, path):
        os.rmdir("." + path)

    def symlink(self, path, path1):
        os.symlink(path, "." + path1)

    def rename(self, path, path1):
        os.rename("." + path, "." + path1)

    def link(self, path, path1):
        os.link("." + path, "." + path1)

    def chmod(self, path, mode):
        os.chmod("." + path, mode)

    def chown(self, path, user, group):
        os.chown("." + path, user, group)

    def truncate(self, path, len):
        f = open("." + path, "a")
        f.truncate(len)
        f.close()

    def mknod(self, path, mode, dev):
        os.mknod("." + path, mode, dev)

    def mkdir(self, path, mode):
        os.mkdir("." + path, mode)

    def utime(self, path, times):
        os.utime("." + path, times)

#    The following utimens method would do the same as the above utime method.
#    We can't make it better though as the Python stdlib doesn't know of
#    subsecond preciseness in acces/modify times.
#  
#    def utimens(self, path, ts_acc, ts_mod):
#      os.utime("." + path, (ts_acc.tv_sec, ts_mod.tv_sec))

    def access(self, path, mode):
        if not os.access("." + path, mode):
            return -EACCES

#    This is how we could add stub extended attribute handlers...
#    (We can't have ones which aptly delegate requests to the underlying fs
#    because Python lacks a standard xattr interface.)
#
#    def getxattr(self, path, name, size):
#        val = name.swapcase() + '@' + path
#        if size == 0:
#            # We are asked for size of the value.
#            return len(val)
#        return val
#
#    def listxattr(self, path, size):
#        # We use the "user" namespace to please XFS utils
#        aa = ["user." + a for a in ("foo", "bar")]
#        if size == 0:
#            # We are asked for size of the attr list, ie. joint size of attrs
#            # plus null separators.
#            return len("".join(aa)) + len(aa)
#        return aa

    def statfs(self):
        """
        Should return an object with statvfs attributes (f_bsize, f_frsize...).
        Eg., the return value of os.statvfs() is such a thing (since py 2.2).
        If you are not reusing an existing statvfs object, start with
        fuse.StatVFS(), and define the attributes.

        To provide usable information (ie., you want sensible df(1)
        output, you are suggested to specify the following attributes:

            - f_bsize - preferred size of file blocks, in bytes
            - f_frsize - fundamental size of file blcoks, in bytes
                [if you have no idea, use the same as blocksize]
            - f_blocks - total number of blocks in the filesystem
            - f_bfree - number of free blocks
            - f_files - total number of file inodes
            - f_ffree - nunber of free file inodes
        """

        return os.statvfs(".")

    def fsinit(self):
        os.chdir(self.root)

    class XmpFile(object):

        def get_server_mtime(self, proto_path):
            return stub.get_mtime(proto_path, _TIMEOUT_SECONDS).mtime

        def get_client_mtime(self, root_path):
            try:
                client_mtime = os.stat(root_path).st_mtime
            except OSError as ose:
                if ose.errno == errno.ENOENT:
                    client_mtime = 0
            return client_mtime

        def get_remote_file(self, root_path, proto_path):
            # TODO: incremental updates with rsync
            temp_filename = None
            with tempfile.NamedTemporaryFile(delete=False) as temp:
                temp_filename = temp.name
                for cont in stub.get_file_contents(proto_path, _TIMEOUT_SECONDS):
                    temp.write(cont.content)
            return temp_filename

        def __init__(self, path, flags, *mode):
            # To find whether the file is modified
            self.isModified = False

            print '****************************************** OPEN'
            print '***********************************Path %s' % path
            proto_path = sankalpa_fs_pb2.Path(path=path)
            server_mtime = self.get_server_mtime(proto_path)
            root_path = _full_path(root, path)
            print '********************************Server_mtime %s' % server_mtime
            if server_mtime != 0:
                client_mtime = self.get_client_mtime(root_path)
                print '***********************************client_mtime %s' % client_mtime
                if server_mtime > client_mtime:
                    print '***********************************Fetching from server '
                    temp_filename = self.get_remote_file(root_path, proto_path)
                    # If the dir path doesnt exsists when the file already exsists.
                    if not os.path.exists(os.path.dirname(root_path)):
                        os.makedirs(os.path.dirname(root_path))
                    os.rename(temp_filename, root_path)
                    # keep the client mtime in sync with server due to
                    # network delays
                    os.utime(root_path, (os.stat(root_path).st_atime, server_mtime))
            self.file = os.fdopen(os.open("." + path, flags, *mode),
                                  flag2mode(flags))
            self.fd = self.file.fileno()
            self.root_path = root_path
            self.path = path

        def read(self, length, offset):
            self.file.seek(offset)
            return self.file.read(length)

        def write(self, buf, offset):
            self.file.seek(offset)
            self.file.write(buf)
            self.isModified = True
            return len(buf)

        def read_file_contents(self):
            print '********** read_file_contents ************'
            yield sankalpa_fs_pb2.Content(content=self.path)

            with open(self.root_path, 'r') as fo:
                while True:
                    string_stream = fo.read(_stream_packet_size)
                    if string_stream:
                        yield sankalpa_fs_pb2.Content(content=string_stream)
                    else:
                        break

        def update_remote_file(self):
            print '********** update_remote_file ************'
            content_iter = self.read_file_contents()
            ack = stub.update_file(content_iter, _TIMEOUT_SECONDS)
            if ack.file_path != self.path or ack.num_bytes != os.stat(self.root_path).st_size:
               print '********** File Update Error ************'
               raise OSError("File Update Error")
            else:
                # Setting the mtime in client to reflect the server
                # This avoid a fetch call after every update
                print '********** File Update mtime ************'
                os.utime(self.root_path, (os.stat(self.root_path).st_atime, ack.server_mtime.mtime))

        def release(self, flags):
            print '********** RELEASE ************'
            print '********** isModified %s ' % self.isModified
            if self.isModified:
                self.update_remote_file()
            self.file.close()

        def _fflush(self):
            if 'w' in self.file.mode or 'a' in self.file.mode:
                self.file.flush()

        def fsync(self, isfsyncfile):
            self._fflush()
            if isfsyncfile and hasattr(os, 'fdatasync'):
                os.fdatasync(self.fd)
            else:
                os.fsync(self.fd)

        def flush(self):
            self._fflush()
            # cf. xmp_flush() in fusexmp_fh.c
            os.close(os.dup(self.fd))

        def fgetattr(self):
            return os.fstat(self.fd)

        def ftruncate(self, len):
            self.file.truncate(len)

        def lock(self, cmd, owner, **kw):
            # The code here is much rather just a demonstration of the locking
            # API than something which actually was seen to be useful.

            # Advisory file locking is pretty messy in Unix, and the Python
            # interface to this doesn't make it better.
            # We can't do fcntl(2)/F_GETLK from Python in a platfrom independent
            # way. The following implementation *might* work under Linux. 
            #
            # if cmd == fcntl.F_GETLK:
            #     import struct
            # 
            #     lockdata = struct.pack('hhQQi', kw['l_type'], os.SEEK_SET,
            #                            kw['l_start'], kw['l_len'], kw['l_pid'])
            #     ld2 = fcntl.fcntl(self.fd, fcntl.F_GETLK, lockdata)
            #     flockfields = ('l_type', 'l_whence', 'l_start', 'l_len', 'l_pid')
            #     uld2 = struct.unpack('hhQQi', ld2)
            #     res = {}
            #     for i in xrange(len(uld2)):
            #          res[flockfields[i]] = uld2[i]
            #  
            #     return fuse.Flock(**res)

            # Convert fcntl-ish lock parameters to Python's weird
            # lockf(3)/flock(2) medley locking API...
            op = { fcntl.F_UNLCK : fcntl.LOCK_UN,
                   fcntl.F_RDLCK : fcntl.LOCK_SH,
                   fcntl.F_WRLCK : fcntl.LOCK_EX }[kw['l_type']]
            if cmd == fcntl.F_GETLK:
                return -EOPNOTSUPP
            elif cmd == fcntl.F_SETLK:
                if op != fcntl.LOCK_UN:
                    op |= fcntl.LOCK_NB
            elif cmd == fcntl.F_SETLKW:
                pass
            else:
                return -EINVAL

            fcntl.lockf(self.fd, op, kw['l_start'], kw['l_len'])


    def main(self, *a, **kw):

        self.file_class = self.XmpFile

        return Fuse.main(self, *a, **kw)


def main():

    global stub, mount_point, root

    channel = implementations.insecure_channel('pc-c220m4-r03-19.wisc.cloudlab.us', 50051)
    stub = sankalpa_fs_pb2.beta_create_SankalpaFS_stub(channel)

    usage = """
Userspace nullfs-alike: mirror the filesystem tree from some point on.

""" + Fuse.fusage

    server = Xmp(version="%prog " + fuse.__version__,
                 usage=usage,
                 dash_s_do='setsingle')

    server.parser.add_option(mountopt="root", metavar="PATH", default='/',
                             help="mirror filesystem from under PATH [default: %default]")
    server.parse(values=server, errex=1)

    mount_point = server.fuse_args.mountpoint
    root = server.root

    try:
        if server.fuse_args.mount_expected():
            os.chdir(server.root)
    except OSError:
        print >> sys.stderr, "can't enter root of underlying filesystem"
        sys.exit(1)

    server.main()


if __name__ == '__main__':
    main()
