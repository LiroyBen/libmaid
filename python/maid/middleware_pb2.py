# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: maid/middleware.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from maid import controller_pb2 as maid_dot_controller__pb2
from maid import connection_pb2 as maid_dot_connection__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='maid/middleware.proto',
  package='maid.proto',
  syntax='proto2',
  serialized_pb=_b('\n\x15maid/middleware.proto\x12\nmaid.proto\x1a\x15maid/controller.proto\x1a\x15maid/connection.proto2\xd7\x03\n\nMiddleware\x12\x45\n\tConnected\x12\x1b.maid.proto.ConnectionProto\x1a\x1b.maid.proto.ConnectionProto\x12H\n\x0c\x44isconnected\x12\x1b.maid.proto.ConnectionProto\x1a\x1b.maid.proto.ConnectionProto\x12J\n\x0eProcessRequest\x12\x1b.maid.proto.ControllerProto\x1a\x1b.maid.proto.ControllerProto\x12K\n\x0fProcessResponse\x12\x1b.maid.proto.ControllerProto\x1a\x1b.maid.proto.ControllerProto\x12N\n\x12ProcessRequestStub\x12\x1b.maid.proto.ControllerProto\x1a\x1b.maid.proto.ControllerProto\x12O\n\x13ProcessResponseStub\x12\x1b.maid.proto.ControllerProto\x1a\x1b.maid.proto.ControllerProtoB\x03\x80\x01\x01')
  ,
  dependencies=[maid_dot_controller__pb2.DESCRIPTOR,maid_dot_connection__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\200\001\001'))
# @@protoc_insertion_point(module_scope)
