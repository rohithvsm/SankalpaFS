#SankalpaFS
Distributed File System running as a FUSE implementing AFSv1 protocol using gRPC (Google's Open Source RPC package) and protobuf

###Requirements: 
- [GRPC](http://www.grpc.io/)
- [Fuse](http://fuse.sourceforge.net/)
- [fuse-python](http://sourceforge.net/projects/fuse/files/fuse-python/0.2.1/)

###To Run:
- ./run_codegen.sh to generate the grpc stub files
- python sankalpa_fsd.py <path-to-dir>
- python sankalpa_fsc.py <path-to-mountpoint> <path-to-cache>
