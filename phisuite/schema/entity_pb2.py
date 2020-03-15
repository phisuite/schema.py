# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: entity.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='entity.proto',
  package='schema',
  syntax='proto3',
  serialized_options=b'\n\023com.phisuite.schemaB\013EntityProtoP\001',
  serialized_pb=b'\n\x0c\x65ntity.proto\x12\x06schema\x1a\x0c\x63ommon.proto\"\x84\x01\n\x06\x45ntity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x1e\n\x06status\x18\x03 \x01(\x0e\x32\x0e.schema.Status\x12\x1b\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\r.schema.Field\x12\x1e\n\x07options\x18\x05 \x03(\x0b\x32\r.schema.Field2\x8c\x02\n\tEntityAPI\x12)\n\x04List\x12\x0f.schema.Options\x1a\x0e.schema.Entity0\x01\x12&\n\x03Get\x12\x0f.schema.Options\x1a\x0e.schema.Entity\x12(\n\x06\x43reate\x12\x0e.schema.Entity\x1a\x0e.schema.Entity\x12(\n\x06Update\x12\x0e.schema.Entity\x1a\x0e.schema.Entity\x12*\n\x08\x41\x63tivate\x12\x0e.schema.Entity\x1a\x0e.schema.Entity\x12,\n\nDeactivate\x12\x0e.schema.Entity\x1a\x0e.schema.EntityB$\n\x13\x63om.phisuite.schemaB\x0b\x45ntityProtoP\x01\x62\x06proto3'
  ,
  dependencies=[common__pb2.DESCRIPTOR,])




_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='schema.Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='schema.Entity.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='schema.Entity.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='schema.Entity.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='schema.Entity.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='schema.Entity.options', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=171,
)

_ENTITY.fields_by_name['status'].enum_type = common__pb2._STATUS
_ENTITY.fields_by_name['data'].message_type = common__pb2._FIELD
_ENTITY.fields_by_name['options'].message_type = common__pb2._FIELD
DESCRIPTOR.message_types_by_name['Entity'] = _ENTITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'entity_pb2'
  # @@protoc_insertion_point(class_scope:schema.Entity)
  })
_sym_db.RegisterMessage(Entity)


DESCRIPTOR._options = None

_ENTITYAPI = _descriptor.ServiceDescriptor(
  name='EntityAPI',
  full_name='schema.EntityAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=174,
  serialized_end=442,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='schema.EntityAPI.List',
    index=0,
    containing_service=None,
    input_type=common__pb2._OPTIONS,
    output_type=_ENTITY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='schema.EntityAPI.Get',
    index=1,
    containing_service=None,
    input_type=common__pb2._OPTIONS,
    output_type=_ENTITY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='schema.EntityAPI.Create',
    index=2,
    containing_service=None,
    input_type=_ENTITY,
    output_type=_ENTITY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='schema.EntityAPI.Update',
    index=3,
    containing_service=None,
    input_type=_ENTITY,
    output_type=_ENTITY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Activate',
    full_name='schema.EntityAPI.Activate',
    index=4,
    containing_service=None,
    input_type=_ENTITY,
    output_type=_ENTITY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Deactivate',
    full_name='schema.EntityAPI.Deactivate',
    index=5,
    containing_service=None,
    input_type=_ENTITY,
    output_type=_ENTITY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENTITYAPI)

DESCRIPTOR.services_by_name['EntityAPI'] = _ENTITYAPI

# @@protoc_insertion_point(module_scope)