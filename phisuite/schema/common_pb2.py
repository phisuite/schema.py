# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='schema',
  syntax='proto3',
  serialized_options=b'\n\023com.phisuite.schemaB\013CommonProtoP\001Z\032github.com/phisuite/schema',
  serialized_pb=b'\n\x0c\x63ommon.proto\x12\x06schema\"e\n\x07Options\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x1e\n\x06status\x18\x03 \x01(\x0e\x32\x0e.schema.Status\x12\x0c\n\x04skip\x18\n \x01(\r\x12\r\n\x05limit\x18\x0b \x01(\r\"\xf6\x01\n\x05\x46ield\x12\x0c\n\x04name\x18\x01 \x01(\t\x12 \n\x04type\x18\x02 \x01(\x0e\x32\x12.schema.Field.Type\x12(\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32\x16.schema.Field.Category\"k\n\x04Type\x12\n\n\x06STRING\x10\x00\x12\n\n\x06NUMBER\x10\x01\x12\x0b\n\x07\x42OOLEAN\x10\x02\x12\x08\n\x04\x46ILE\x10\n\x12\n\n\x06\x46OLDER\x10\x0b\x12\t\n\x05\x45MAIL\x10\x14\x12\x08\n\x04\x44\x41TE\x10\x15\x12\x08\n\x04TIME\x10\x16\x12\t\n\x05\x43OLOR\x10\x17\"&\n\x08\x43\x61tegory\x12\x0c\n\x08REQUIRED\x10\x00\x12\x0c\n\x08OPTIONAL\x10\x01*9\n\x06Status\x12\x0f\n\x0bUNACTIVATED\x10\x00\x12\r\n\tACTIVATED\x10\x01\x12\x0f\n\x0b\x44\x45\x41\x43TIVATED\x10\x02\x42@\n\x13\x63om.phisuite.schemaB\x0b\x43ommonProtoP\x01Z\x1agithub.com/phisuite/schemab\x06proto3'
)

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='schema.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNACTIVATED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVATED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEACTIVATED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=376,
  serialized_end=433,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
UNACTIVATED = 0
ACTIVATED = 1
DEACTIVATED = 2


_FIELD_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='schema.Field.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STRING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUMBER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILE', index=3, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOLDER', index=4, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMAIL', index=5, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE', index=6, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIME', index=7, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLOR', index=8, number=23,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=227,
  serialized_end=334,
)
_sym_db.RegisterEnumDescriptor(_FIELD_TYPE)

_FIELD_CATEGORY = _descriptor.EnumDescriptor(
  name='Category',
  full_name='schema.Field.Category',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REQUIRED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPTIONAL', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=336,
  serialized_end=374,
)
_sym_db.RegisterEnumDescriptor(_FIELD_CATEGORY)


_OPTIONS = _descriptor.Descriptor(
  name='Options',
  full_name='schema.Options',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='schema.Options.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='schema.Options.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='schema.Options.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skip', full_name='schema.Options.skip', index=3,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='schema.Options.limit', index=4,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=24,
  serialized_end=125,
)


_FIELD = _descriptor.Descriptor(
  name='Field',
  full_name='schema.Field',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='schema.Field.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='schema.Field.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='schema.Field.category', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FIELD_TYPE,
    _FIELD_CATEGORY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=374,
)

_OPTIONS.fields_by_name['status'].enum_type = _STATUS
_FIELD.fields_by_name['type'].enum_type = _FIELD_TYPE
_FIELD.fields_by_name['category'].enum_type = _FIELD_CATEGORY
_FIELD_TYPE.containing_type = _FIELD
_FIELD_CATEGORY.containing_type = _FIELD
DESCRIPTOR.message_types_by_name['Options'] = _OPTIONS
DESCRIPTOR.message_types_by_name['Field'] = _FIELD
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Options = _reflection.GeneratedProtocolMessageType('Options', (_message.Message,), {
  'DESCRIPTOR' : _OPTIONS,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:schema.Options)
  })
_sym_db.RegisterMessage(Options)

Field = _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), {
  'DESCRIPTOR' : _FIELD,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:schema.Field)
  })
_sym_db.RegisterMessage(Field)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
