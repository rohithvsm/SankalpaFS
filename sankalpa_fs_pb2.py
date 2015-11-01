# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sankalpa_fs.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sankalpa_fs.proto',
  package='sankalpafs',
  syntax='proto3',
  serialized_pb=b'\n\x11sankalpa_fs.proto\x12\nsankalpafs\"\x14\n\x04Path\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x16\n\x05MTime\x12\r\n\x05mtime\x18\x01 \x01(\x02\"\x1a\n\x07\x43ontent\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"\x1d\n\x08NumBytes\x12\x11\n\tnum_bytes\x18\x01 \x01(\x03\"\x18\n\x06Status\x12\x0e\n\x06status\x18\x01 \x01(\r2\xf0\x01\n\nSankalpaFS\x12\x32\n\tget_mtime\x12\x10.sankalpafs.Path\x1a\x11.sankalpafs.MTime\"\x00\x12>\n\x11get_file_contents\x12\x10.sankalpafs.Path\x1a\x13.sankalpafs.Content\"\x00\x30\x01\x12<\n\x0bupdate_file\x12\x13.sankalpafs.Content\x1a\x14.sankalpafs.NumBytes\"\x00(\x01\x12\x30\n\x06\x64\x65lete\x12\x10.sankalpafs.Path\x1a\x12.sankalpafs.Status\"\x00\x42\x0f\n\x07\x65x.grpc\xa2\x02\x03RTGb\x06proto3'
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PATH = _descriptor.Descriptor(
  name='Path',
  full_name='sankalpafs.Path',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='sankalpafs.Path.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=53,
)


_MTIME = _descriptor.Descriptor(
  name='MTime',
  full_name='sankalpafs.MTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mtime', full_name='sankalpafs.MTime.mtime', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=77,
)


_CONTENT = _descriptor.Descriptor(
  name='Content',
  full_name='sankalpafs.Content',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='sankalpafs.Content.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=105,
)


_NUMBYTES = _descriptor.Descriptor(
  name='NumBytes',
  full_name='sankalpafs.NumBytes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_bytes', full_name='sankalpafs.NumBytes.num_bytes', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=136,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='sankalpafs.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='sankalpafs.Status.status', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=162,
)

DESCRIPTOR.message_types_by_name['Path'] = _PATH
DESCRIPTOR.message_types_by_name['MTime'] = _MTIME
DESCRIPTOR.message_types_by_name['Content'] = _CONTENT
DESCRIPTOR.message_types_by_name['NumBytes'] = _NUMBYTES
DESCRIPTOR.message_types_by_name['Status'] = _STATUS

Path = _reflection.GeneratedProtocolMessageType('Path', (_message.Message,), dict(
  DESCRIPTOR = _PATH,
  __module__ = 'sankalpa_fs_pb2'
  # @@protoc_insertion_point(class_scope:sankalpafs.Path)
  ))
_sym_db.RegisterMessage(Path)

MTime = _reflection.GeneratedProtocolMessageType('MTime', (_message.Message,), dict(
  DESCRIPTOR = _MTIME,
  __module__ = 'sankalpa_fs_pb2'
  # @@protoc_insertion_point(class_scope:sankalpafs.MTime)
  ))
_sym_db.RegisterMessage(MTime)

Content = _reflection.GeneratedProtocolMessageType('Content', (_message.Message,), dict(
  DESCRIPTOR = _CONTENT,
  __module__ = 'sankalpa_fs_pb2'
  # @@protoc_insertion_point(class_scope:sankalpafs.Content)
  ))
_sym_db.RegisterMessage(Content)

NumBytes = _reflection.GeneratedProtocolMessageType('NumBytes', (_message.Message,), dict(
  DESCRIPTOR = _NUMBYTES,
  __module__ = 'sankalpa_fs_pb2'
  # @@protoc_insertion_point(class_scope:sankalpafs.NumBytes)
  ))
_sym_db.RegisterMessage(NumBytes)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'sankalpa_fs_pb2'
  # @@protoc_insertion_point(class_scope:sankalpafs.Status)
  ))
_sym_db.RegisterMessage(Status)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), b'\n\007ex.grpc\242\002\003RTG')
import abc
from grpc.beta import implementations as beta_implementations
from grpc.early_adopter import implementations as early_adopter_implementations
from grpc.framework.alpha import utilities as alpha_utilities
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
class EarlyAdopterSankalpaFSServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def get_mtime(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def get_file_contents(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def update_file(self, request_iterator, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def delete(self, request, context):
    raise NotImplementedError()
class EarlyAdopterSankalpaFSServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterSankalpaFSStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def get_mtime(self, request):
    raise NotImplementedError()
  get_mtime.async = None
  @abc.abstractmethod
  def get_file_contents(self, request):
    raise NotImplementedError()
  get_file_contents.async = None
  @abc.abstractmethod
  def update_file(self, request_iterator):
    raise NotImplementedError()
  update_file.async = None
  @abc.abstractmethod
  def delete(self, request):
    raise NotImplementedError()
  delete.async = None
def early_adopter_create_SankalpaFS_server(servicer, port, private_key=None, certificate_chain=None):
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  method_service_descriptions = {
    "delete": alpha_utilities.unary_unary_service_description(
      servicer.delete,
      sankalpa_fs_pb2.Path.FromString,
      sankalpa_fs_pb2.Status.SerializeToString,
    ),
    "get_file_contents": alpha_utilities.unary_stream_service_description(
      servicer.get_file_contents,
      sankalpa_fs_pb2.Path.FromString,
      sankalpa_fs_pb2.Content.SerializeToString,
    ),
    "get_mtime": alpha_utilities.unary_unary_service_description(
      servicer.get_mtime,
      sankalpa_fs_pb2.Path.FromString,
      sankalpa_fs_pb2.MTime.SerializeToString,
    ),
    "update_file": alpha_utilities.stream_unary_service_description(
      servicer.update_file,
      sankalpa_fs_pb2.Content.FromString,
      sankalpa_fs_pb2.NumBytes.SerializeToString,
    ),
  }
  return early_adopter_implementations.server("sankalpafs.SankalpaFS", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_SankalpaFS_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  method_invocation_descriptions = {
    "delete": alpha_utilities.unary_unary_invocation_description(
      sankalpa_fs_pb2.Path.SerializeToString,
      sankalpa_fs_pb2.Status.FromString,
    ),
    "get_file_contents": alpha_utilities.unary_stream_invocation_description(
      sankalpa_fs_pb2.Path.SerializeToString,
      sankalpa_fs_pb2.Content.FromString,
    ),
    "get_mtime": alpha_utilities.unary_unary_invocation_description(
      sankalpa_fs_pb2.Path.SerializeToString,
      sankalpa_fs_pb2.MTime.FromString,
    ),
    "update_file": alpha_utilities.stream_unary_invocation_description(
      sankalpa_fs_pb2.Content.SerializeToString,
      sankalpa_fs_pb2.NumBytes.FromString,
    ),
  }
  return early_adopter_implementations.stub("sankalpafs.SankalpaFS", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)

class BetaSankalpaFSServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def get_mtime(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def get_file_contents(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def update_file(self, request_iterator, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def delete(self, request, context):
    raise NotImplementedError()

class BetaSankalpaFSStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def get_mtime(self, request, timeout):
    raise NotImplementedError()
  get_mtime.future = None
  @abc.abstractmethod
  def get_file_contents(self, request, timeout):
    raise NotImplementedError()
  @abc.abstractmethod
  def update_file(self, request_iterator, timeout):
    raise NotImplementedError()
  update_file.future = None
  @abc.abstractmethod
  def delete(self, request, timeout):
    raise NotImplementedError()
  delete.future = None

def beta_create_SankalpaFS_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  request_deserializers = {
    ('sankalpafs.SankalpaFS', 'delete'): sankalpa_fs_pb2.Path.FromString,
    ('sankalpafs.SankalpaFS', 'get_file_contents'): sankalpa_fs_pb2.Path.FromString,
    ('sankalpafs.SankalpaFS', 'get_mtime'): sankalpa_fs_pb2.Path.FromString,
    ('sankalpafs.SankalpaFS', 'update_file'): sankalpa_fs_pb2.Content.FromString,
  }
  response_serializers = {
    ('sankalpafs.SankalpaFS', 'delete'): sankalpa_fs_pb2.Status.SerializeToString,
    ('sankalpafs.SankalpaFS', 'get_file_contents'): sankalpa_fs_pb2.Content.SerializeToString,
    ('sankalpafs.SankalpaFS', 'get_mtime'): sankalpa_fs_pb2.MTime.SerializeToString,
    ('sankalpafs.SankalpaFS', 'update_file'): sankalpa_fs_pb2.NumBytes.SerializeToString,
  }
  method_implementations = {
    ('sankalpafs.SankalpaFS', 'delete'): face_utilities.unary_unary_inline(servicer.delete),
    ('sankalpafs.SankalpaFS', 'get_file_contents'): face_utilities.unary_stream_inline(servicer.get_file_contents),
    ('sankalpafs.SankalpaFS', 'get_mtime'): face_utilities.unary_unary_inline(servicer.get_mtime),
    ('sankalpafs.SankalpaFS', 'update_file'): face_utilities.stream_unary_inline(servicer.update_file),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_SankalpaFS_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  import sankalpa_fs_pb2
  request_serializers = {
    ('sankalpafs.SankalpaFS', 'delete'): sankalpa_fs_pb2.Path.SerializeToString,
    ('sankalpafs.SankalpaFS', 'get_file_contents'): sankalpa_fs_pb2.Path.SerializeToString,
    ('sankalpafs.SankalpaFS', 'get_mtime'): sankalpa_fs_pb2.Path.SerializeToString,
    ('sankalpafs.SankalpaFS', 'update_file'): sankalpa_fs_pb2.Content.SerializeToString,
  }
  response_deserializers = {
    ('sankalpafs.SankalpaFS', 'delete'): sankalpa_fs_pb2.Status.FromString,
    ('sankalpafs.SankalpaFS', 'get_file_contents'): sankalpa_fs_pb2.Content.FromString,
    ('sankalpafs.SankalpaFS', 'get_mtime'): sankalpa_fs_pb2.MTime.FromString,
    ('sankalpafs.SankalpaFS', 'update_file'): sankalpa_fs_pb2.NumBytes.FromString,
  }
  cardinalities = {
    'delete': cardinality.Cardinality.UNARY_UNARY,
    'get_file_contents': cardinality.Cardinality.UNARY_STREAM,
    'get_mtime': cardinality.Cardinality.UNARY_UNARY,
    'update_file': cardinality.Cardinality.STREAM_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'sankalpafs.SankalpaFS', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
