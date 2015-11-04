"""The Python implementation of the gRPC Sankalpa FS server."""

import sys
import errno
import sankalpa_fs_pb2
import os
import time
import tempfile

#TODO:
# version number as extended file attributes
# Multiple clients
# Exception handling

def _full_path(base_path, relative_path):
    if relative_path.startswith('/'):
        relative_path = relative_path[1:]
    return os.path.join(base_path, relative_path)

class SankalpaFSServicer(sankalpa_fs_pb2.BetaSankalpaFSServicer):
    """Provides methods that implement functionality of Sankalpa FS server."""

    def __init__(self, storage_dir):
        self.__base_dir = storage_dir
        #TODO: check for correct value
        self.__stream_packet_size = 64 * 1024  # TCP packet size
        self.__stream_packet_size -= 60  # maximum TCP header size
        self.__stream_packet_size -= 192  # maximum IPv4 header size
        self.__stream_packet_size -= 24  # Ethernet header size

    def get_mtime(self, Path, context):
        print '********** in get_mtime ************'
        print '********** %s' % _full_path(self.__base_dir, Path.path)
        try:
            mt = os.stat(_full_path(self.__base_dir, Path.path)).st_mtime
        except OSError, e:
            if e.errno == errno.ENOENT:
                mt = 0
        print '********** %s' % mt
        return sankalpa_fs_pb2.MTime(mtime = mt)

    def get_file_contents(self, Path, context):
        print '********** in get_file_contents ************'
        print '********** %s' % _full_path(self.__base_dir, Path.path)
        with open(_full_path(self.__base_dir, Path.path), 'r') as fo:
            while True:
                string_stream = fo.read(self.__stream_packet_size)
                if string_stream:
                    yield sankalpa_fs_pb2.Content(content=string_stream)
                else:
                    break

    def update_file(self, Content_iter, context):
        file_path_rel = None
        print '********** update_file ************'
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            temp_filename = temp.name
            counter = 0
            # TODO: try multiple for loops and slicing
            for cont in Content_iter:
                if counter == 0:
                    file_path_rel = cont.content
                    counter += 1
                    continue
                temp.write(cont.content)
            print '********** update_file temp file name %s' % temp.name
        print '********** update_file name %s' % file_path_rel
        file_path = _full_path(self.__base_dir, file_path_rel)
        print '********** update_file name %s' % file_path
        os.rename(temp_filename, file_path)
        #TODO : DO we need to return numb_bytes ?
        print '********** update_file size %s' % os.stat(file_path).st_size
        stat = os.stat(file_path)
        return sankalpa_fs_pb2.UpdateAck(file_path=file_path_rel,
                                         num_bytes=stat.st_size,
                                         server_mtime=sankalpa_fs_pb2.MTime(mtime = stat.st_mtime))

    def delete(self, Path, context):
        try:
            os.remove(_full_path(self.__base_dir, Path.path))
            return sankalpa_fs_pb2.Status(status=0)
        except OSError as ose:
            return sankalpa_fs_pb2.Status(status=ose.errno)

    def mkdir(self, Path, context):
        try:
            os.mkdir(_full_path(self.__base_dir, Path.path))
            return sankalpa_fs_pb2.Status(status=0)
        except OSError as ose:
            return sankalpa_fs_pb2.Status(status=ose.errno)

    def rmdir(self, Path, context):
        try:
            os.rmdir(_full_path(self.__base_dir, Path.path))
            return sankalpa_fs_pb2.Status(status=0)
        except OSError as ose:
            return sankalpa_fs_pb2.Status(status=ose.errno)

    def readdir(self, Path, context):
        print '********** readdir ************ %s' % Path.path
        ro = sankalpa_fs_pb2.ListDir()
        ro.status = 0
        direntries = None
        try:
            direntries = os.listdir(_full_path(self.__base_dir, Path.path))
        except OSError as ose:
            ro.status = ose.errno
            print '**************** ro %s' % ro.status
            return ro
        for direntry in direntries:
            ro.dir.append(direntry)
        print '**************** ro status %s' % ro.status
        print '**************** ro dir %s' % ro.dir
        return ro

    def getattr(self, Path, context):
        print '********** getattr ************ %s' % Path.path
        ro = sankalpa_fs_pb2.Stat()
        ro.status = 0
        try:
            server_file_stat = os.lstat(_full_path(self.__base_dir, Path.path))
        except OSError as ose:
            ro.status = ose.errno
            print '**************** ro status %s' % ro.status
            return ro
        ro.st_mode = server_file_stat.st_mode
        ro.st_ino = server_file_stat.st_ino
        ro.st_dev = server_file_stat.st_dev
        ro.st_nlink = server_file_stat.st_nlink
        ro.st_uid = server_file_stat.st_uid
        ro.st_gid = server_file_stat.st_gid
        ro.st_size = server_file_stat.st_size
        ro.st_atime = server_file_stat.st_atime
        ro.st_mtime = server_file_stat.st_mtime
        ro.st_ctime  = server_file_stat.st_ctime
        print '**************** ro status %s' % ro.status
        print '**************** ro %s' % ro
        return ro
        
def serve():
    storage_dir = sys.argv[1]
    if not storage_dir.startswith('/'):
        sys.exit("Storage directory must start with /")
    if not os.path.exists(storage_dir):
        os.makedirs(storage_dir)
    server = sankalpa_fs_pb2.beta_create_SankalpaFS_server(SankalpaFSServicer(sys.argv[1]))
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(24 * 60 * 60)
    except KeyboardInterrupt:
        server.stop()

if __name__ == '__main__':
    serve()
