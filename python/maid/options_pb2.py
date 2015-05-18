# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: maid/options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='maid/options.proto',
  package='maid.proto',
  syntax='proto2',
  serialized_pb=_b('\n\x12maid/options.proto\x12\nmaid.proto\x1a google/protobuf/descriptor.proto\"$\n\x12MaidServiceOptions\x12\x0e\n\x06notify\x18\x01 \x01(\x08\"9\n\x11MaidMethodOptions\x12\x0e\n\x06notify\x18\x01 \x01(\x08\x12\x14\n\x08time_out\x18\x02 \x01(\x03:\x02-1:Y\n\x0fservice_options\x12\x1f.google.protobuf.ServiceOptions\x18\xe9\x07 \x01(\x0b\x32\x1e.maid.proto.MaidServiceOptions:V\n\x0emethod_options\x12\x1e.google.protobuf.MethodOptions\x18\xe9\x07 \x01(\x0b\x32\x1d.maid.proto.MaidMethodOptions')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


SERVICE_OPTIONS_FIELD_NUMBER = 1001
service_options = _descriptor.FieldDescriptor(
  name='service_options', full_name='maid.proto.service_options', index=0,
  number=1001, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
METHOD_OPTIONS_FIELD_NUMBER = 1001
method_options = _descriptor.FieldDescriptor(
  name='method_options', full_name='maid.proto.method_options', index=1,
  number=1001, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_MAIDSERVICEOPTIONS = _descriptor.Descriptor(
  name='MaidServiceOptions',
  full_name='maid.proto.MaidServiceOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notify', full_name='maid.proto.MaidServiceOptions.notify', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=104,
)


_MAIDMETHODOPTIONS = _descriptor.Descriptor(
  name='MaidMethodOptions',
  full_name='maid.proto.MaidMethodOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notify', full_name='maid.proto.MaidMethodOptions.notify', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_out', full_name='maid.proto.MaidMethodOptions.time_out', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=-1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=163,
)

DESCRIPTOR.message_types_by_name['MaidServiceOptions'] = _MAIDSERVICEOPTIONS
DESCRIPTOR.message_types_by_name['MaidMethodOptions'] = _MAIDMETHODOPTIONS
DESCRIPTOR.extensions_by_name['service_options'] = service_options
DESCRIPTOR.extensions_by_name['method_options'] = method_options

MaidServiceOptions = _reflection.GeneratedProtocolMessageType('MaidServiceOptions', (_message.Message,), dict(
  DESCRIPTOR = _MAIDSERVICEOPTIONS,
  __module__ = 'maid.options_pb2'
  # @@protoc_insertion_point(class_scope:maid.proto.MaidServiceOptions)
  ))
_sym_db.RegisterMessage(MaidServiceOptions)

MaidMethodOptions = _reflection.GeneratedProtocolMessageType('MaidMethodOptions', (_message.Message,), dict(
  DESCRIPTOR = _MAIDMETHODOPTIONS,
  __module__ = 'maid.options_pb2'
  # @@protoc_insertion_point(class_scope:maid.proto.MaidMethodOptions)
  ))
_sym_db.RegisterMessage(MaidMethodOptions)

service_options.message_type = _MAIDSERVICEOPTIONS
google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(service_options)
method_options.message_type = _MAIDMETHODOPTIONS
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(method_options)

# @@protoc_insertion_point(module_scope)
