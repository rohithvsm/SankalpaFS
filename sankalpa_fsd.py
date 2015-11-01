"""The Python implementation of the gRPC Sankalpa FS server."""

import sys
import sankalpa_fs_pb2
import os
import time

#TODO:
# version number as extended file attributes
# Multiple clients
# Exception handling

class SankalpaFSServicer(sankalpa_fs_pb2.BetaSankalpaFSServicer):
    """Provides methods that implement functionality of Sankalpa FS server."""

    def __init__(self, storage_dir):
        self.__base_dir = storage_dir

        self.__stream_packet_size = 64 * 1024  # TCP packet size
        self.__stream_packet_size -= 60  # maximum TCP header size
        self.__stream_packet_size -= 192  # maximum IPv4 header size
        self.__stream_packet_size -= 24  # Ethernet header size

    def get_mtime(self, Path):
        print '********** in get_mtime ************'
        return self.stat(os.path.join(self.__base_dir, Path.path)).st_mtime

    def get_file_contents(self, Path):
        with open(os.path.join(self.__base_dir, Path.path, 'rb')) as fo:
            while True:
                byte_stream = fo.read(self.__stream_packet_size)
                if byte_stream:
                    yield byte_stream
                else:
                    break

    def update_file(self, File):
        file_name = None

        with tempfile.NamedTemporaryFile() as temp:
            counter = 0
            # TODO: try multiple for loops and slicing
            for cont in content:
                if counter == 0:
                    file_name = cont
                    counter += 1
                    continue
                temp.write(File.content)
            os.rename(NamedTemporaryFile.name, os.path.join(self.__base_dir
                                                           ,file_name))

    def delete(self, Path):
        os.remove(os.path.join(self.__base_dir, Path.path))
        
def serve():
    storage_dir = sys.argv[1]
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
