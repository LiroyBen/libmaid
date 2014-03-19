# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='controller.proto',
  package='maid.proto',
  serialized_pb='\n\x10\x63ontroller.proto\x12\nmaid.proto\"\x97\x01\n\x0e\x43ontrollerMeta\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x13\n\x0bmethod_name\x18\x02 \x01(\t\x12\x13\n\x0btransmit_id\x18\x03 \x01(\r\x12\x0c\n\x04stub\x18\x04 \x01(\x08\x12\x13\n\x0bis_canceled\x18\x05 \x01(\x08\x12\x0e\n\x06\x66\x61iled\x18\x06 \x01(\x08\x12\x12\n\nerror_text\x18\x07 \x01(\t')




_CONTROLLERMETA = descriptor.Descriptor(
  name='ControllerMeta',
  full_name='maid.proto.ControllerMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='service_name', full_name='maid.proto.ControllerMeta.service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='method_name', full_name='maid.proto.ControllerMeta.method_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='transmit_id', full_name='maid.proto.ControllerMeta.transmit_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='stub', full_name='maid.proto.ControllerMeta.stub', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_canceled', full_name='maid.proto.ControllerMeta.is_canceled', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='failed', full_name='maid.proto.ControllerMeta.failed', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='error_text', full_name='maid.proto.ControllerMeta.error_text', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=33,
  serialized_end=184,
)

DESCRIPTOR.message_types_by_name['ControllerMeta'] = _CONTROLLERMETA

class ControllerMeta(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONTROLLERMETA
  
  # @@protoc_insertion_point(class_scope:maid.proto.ControllerMeta)

# @@protoc_insertion_point(module_scope)
