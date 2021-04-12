# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syft_proto/messaging/v1/message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from syft_proto.execution.v1 import computation_action_pb2 as syft__proto_dot_execution_dot_v1_dot_computation__action__pb2
from syft_proto.execution.v1 import communication_action_pb2 as syft__proto_dot_execution_dot_v1_dot_communication__action__pb2
from syft_proto.types.syft.v1 import id_pb2 as syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2
from syft_proto.types.torch.v1 import tensor_pb2 as syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__pb2
from syft_proto.types.syft.v1 import arg_pb2 as syft__proto_dot_types_dot_syft_dot_v1_dot_arg__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='syft_proto/messaging/v1/message.proto',
  package='syft_proto.messaging.v1',
  syntax='proto3',
  serialized_options=b'\n$org.openmined.syftproto.messaging.v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%syft_proto/messaging/v1/message.proto\x12\x17syft_proto.messaging.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x30syft_proto/execution/v1/computation_action.proto\x1a\x32syft_proto/execution/v1/communication_action.proto\x1a!syft_proto/types/syft/v1/id.proto\x1a&syft_proto/types/torch/v1/tensor.proto\x1a\"syft_proto/types/syft/v1/arg.proto\"\xd8\x07\n\x0bSyftMessage\x12\x46\n\x12\x63ontents_empty_msg\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00R\x10\x63ontentsEmptyMsg\x12\x63\n\x13\x63ontents_delete_msg\x18\x02 \x01(\x0b\x32\x31.syft_proto.messaging.v1.ForceObjectDeleteMessageH\x00R\x11\x63ontentsDeleteMsg\x12_\n\x16\x63ontents_get_shape_msg\x18\x03 \x01(\x0b\x32(.syft_proto.messaging.v1.GetShapeMessageH\x00R\x13\x63ontentsGetShapeMsg\x12Y\n\x14\x63ontents_is_none_msg\x18\x04 \x01(\x0b\x32&.syft_proto.messaging.v1.IsNoneMessageH\x00R\x11\x63ontentsIsNoneMsg\x12X\n\x13\x63ontents_object_msg\x18\x05 \x01(\x0b\x32&.syft_proto.messaging.v1.ObjectMessageH\x00R\x11\x63ontentsObjectMsg\x12n\n\x1b\x63ontents_object_request_msg\x18\x06 \x01(\x0b\x32-.syft_proto.messaging.v1.ObjectRequestMessageH\x00R\x18\x63ontentsObjectRequestMsg\x12\x66\n\x17\x63ontents_tensor_cmd_msg\x18\x07 \x01(\x0b\x32-.syft_proto.messaging.v1.TensorCommandMessageH\x00R\x14\x63ontentsTensorCmdMsg\x12`\n\x15\x63ontents_plan_cmd_msg\x18\x08 \x01(\x0b\x32+.syft_proto.messaging.v1.PlanCommandMessageH\x00R\x12\x63ontentsPlanCmdMsg\x12\x66\n\x17\x63ontents_worker_cmd_msg\x18\t \x01(\x0b\x32-.syft_proto.messaging.v1.WorkerCommandMessageH\x00R\x14\x63ontentsWorkerCmdMsg\x12X\n\x13\x63ontents_search_msg\x18\n \x01(\x0b\x32&.syft_proto.messaging.v1.SearchMessageH\x00R\x11\x63ontentsSearchMsgB\n\n\x08\x63ontents\"J\n\rIsNoneMessage\x12\x39\n\tobject_id\x18\x01 \x01(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\x08objectId\"O\n\rObjectMessage\x12>\n\x06tensor\x18\x01 \x01(\x0b\x32&.syft_proto.types.torch.v1.TorchTensorR\x06tensor\"\xc6\x01\n\x14TensorCommandMessage\x12N\n\x0b\x63omputation\x18\x01 \x01(\x0b\x32*.syft_proto.execution.v1.ComputationActionH\x00R\x0b\x63omputation\x12T\n\rcommunication\x18\x02 \x01(\x0b\x32,.syft_proto.execution.v1.CommunicationActionH\x00R\rcommunicationB\x08\n\x06\x61\x63tion\"W\n\x18\x46orceObjectDeleteMessage\x12;\n\nobject_ids\x18\x01 \x03(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\tobjectIds\"L\n\x0fGetShapeMessage\x12\x39\n\tobject_id\x18\x01 \x01(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\x08objectId\"i\n\x14ObjectRequestMessage\x12\x39\n\tobject_id\x18\x01 \x01(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\x08objectId\x12\x16\n\x06reason\x18\x02 \x01(\tR\x06reason\"j\n\x12PlanCommandMessage\x12!\n\x0c\x63ommand_name\x18\x01 \x01(\tR\x0b\x63ommandName\x12\x31\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\x1d.syft_proto.types.syft.v1.ArgR\x04\x61rgs\"l\n\x14WorkerCommandMessage\x12!\n\x0c\x63ommand_name\x18\x01 \x01(\tR\x0b\x63ommandName\x12\x31\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\x1d.syft_proto.types.syft.v1.ArgR\x04\x61rgs\"C\n\rSearchMessage\x12\x32\n\x05query\x18\x01 \x03(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\x05queryB&\n$org.openmined.syftproto.messaging.v1b\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,syft__proto_dot_execution_dot_v1_dot_computation__action__pb2.DESCRIPTOR,syft__proto_dot_execution_dot_v1_dot_communication__action__pb2.DESCRIPTOR,syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2.DESCRIPTOR,syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__pb2.DESCRIPTOR,syft__proto_dot_types_dot_syft_dot_v1_dot_arg__pb2.DESCRIPTOR,])




_SYFTMESSAGE = _descriptor.Descriptor(
  name='SyftMessage',
  full_name='syft_proto.messaging.v1.SyftMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='contents_empty_msg', full_name='syft_proto.messaging.v1.SyftMessage.contents_empty_msg', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsEmptyMsg', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_delete_msg', full_name='syft_proto.messaging.v1.SyftMessage.contents_delete_msg', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsDeleteMsg', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_get_shape_msg', full_name='syft_proto.messaging.v1.SyftMessage.contents_get_shape_msg', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsGetShapeMsg', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_is_none_msg', full_name='syft_proto.messaging.v1.SyftMessage.contents_is_none_msg', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsIsNoneMsg', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_object_msg', full_name='syft_proto.messaging.v1.SyftMessage.contents_object_msg', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsObjectMsg', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_object_request_msg', full_name='syft_proto.messaging.v1.SyftMessage.contents_object_request_msg', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsObjectRequestMsg', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_tensor_cmd_msg', full_name='syft_proto.messaging.v1.SyftMessage.contents_tensor_cmd_msg', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsTensorCmdMsg', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_plan_cmd_msg', full_name='syft_proto.messaging.v1.SyftMessage.contents_plan_cmd_msg', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsPlanCmdMsg', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_worker_cmd_msg', full_name='syft_proto.messaging.v1.SyftMessage.contents_worker_cmd_msg', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsWorkerCmdMsg', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_search_msg', full_name='syft_proto.messaging.v1.SyftMessage.contents_search_msg', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsSearchMsg', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='contents', full_name='syft_proto.messaging.v1.SyftMessage.contents',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=309,
  serialized_end=1293,
)


_ISNONEMESSAGE = _descriptor.Descriptor(
  name='IsNoneMessage',
  full_name='syft_proto.messaging.v1.IsNoneMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='syft_proto.messaging.v1.IsNoneMessage.object_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='objectId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1295,
  serialized_end=1369,
)


_OBJECTMESSAGE = _descriptor.Descriptor(
  name='ObjectMessage',
  full_name='syft_proto.messaging.v1.ObjectMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor', full_name='syft_proto.messaging.v1.ObjectMessage.tensor', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tensor', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1371,
  serialized_end=1450,
)


_TENSORCOMMANDMESSAGE = _descriptor.Descriptor(
  name='TensorCommandMessage',
  full_name='syft_proto.messaging.v1.TensorCommandMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='computation', full_name='syft_proto.messaging.v1.TensorCommandMessage.computation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='computation', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='communication', full_name='syft_proto.messaging.v1.TensorCommandMessage.communication', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='communication', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='action', full_name='syft_proto.messaging.v1.TensorCommandMessage.action',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1453,
  serialized_end=1651,
)


_FORCEOBJECTDELETEMESSAGE = _descriptor.Descriptor(
  name='ForceObjectDeleteMessage',
  full_name='syft_proto.messaging.v1.ForceObjectDeleteMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_ids', full_name='syft_proto.messaging.v1.ForceObjectDeleteMessage.object_ids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='objectIds', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1653,
  serialized_end=1740,
)


_GETSHAPEMESSAGE = _descriptor.Descriptor(
  name='GetShapeMessage',
  full_name='syft_proto.messaging.v1.GetShapeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='syft_proto.messaging.v1.GetShapeMessage.object_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='objectId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1742,
  serialized_end=1818,
)


_OBJECTREQUESTMESSAGE = _descriptor.Descriptor(
  name='ObjectRequestMessage',
  full_name='syft_proto.messaging.v1.ObjectRequestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='syft_proto.messaging.v1.ObjectRequestMessage.object_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='objectId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reason', full_name='syft_proto.messaging.v1.ObjectRequestMessage.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='reason', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1820,
  serialized_end=1925,
)


_PLANCOMMANDMESSAGE = _descriptor.Descriptor(
  name='PlanCommandMessage',
  full_name='syft_proto.messaging.v1.PlanCommandMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='command_name', full_name='syft_proto.messaging.v1.PlanCommandMessage.command_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='commandName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='args', full_name='syft_proto.messaging.v1.PlanCommandMessage.args', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='args', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1927,
  serialized_end=2033,
)


_WORKERCOMMANDMESSAGE = _descriptor.Descriptor(
  name='WorkerCommandMessage',
  full_name='syft_proto.messaging.v1.WorkerCommandMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='command_name', full_name='syft_proto.messaging.v1.WorkerCommandMessage.command_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='commandName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='args', full_name='syft_proto.messaging.v1.WorkerCommandMessage.args', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='args', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=2035,
  serialized_end=2143,
)


_SEARCHMESSAGE = _descriptor.Descriptor(
  name='SearchMessage',
  full_name='syft_proto.messaging.v1.SearchMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='syft_proto.messaging.v1.SearchMessage.query', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='query', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=2145,
  serialized_end=2212,
)

_SYFTMESSAGE.fields_by_name['contents_empty_msg'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_SYFTMESSAGE.fields_by_name['contents_delete_msg'].message_type = _FORCEOBJECTDELETEMESSAGE
_SYFTMESSAGE.fields_by_name['contents_get_shape_msg'].message_type = _GETSHAPEMESSAGE
_SYFTMESSAGE.fields_by_name['contents_is_none_msg'].message_type = _ISNONEMESSAGE
_SYFTMESSAGE.fields_by_name['contents_object_msg'].message_type = _OBJECTMESSAGE
_SYFTMESSAGE.fields_by_name['contents_object_request_msg'].message_type = _OBJECTREQUESTMESSAGE
_SYFTMESSAGE.fields_by_name['contents_tensor_cmd_msg'].message_type = _TENSORCOMMANDMESSAGE
_SYFTMESSAGE.fields_by_name['contents_plan_cmd_msg'].message_type = _PLANCOMMANDMESSAGE
_SYFTMESSAGE.fields_by_name['contents_worker_cmd_msg'].message_type = _WORKERCOMMANDMESSAGE
_SYFTMESSAGE.fields_by_name['contents_search_msg'].message_type = _SEARCHMESSAGE
_SYFTMESSAGE.oneofs_by_name['contents'].fields.append(
  _SYFTMESSAGE.fields_by_name['contents_empty_msg'])
_SYFTMESSAGE.fields_by_name['contents_empty_msg'].containing_oneof = _SYFTMESSAGE.oneofs_by_name['contents']
_SYFTMESSAGE.oneofs_by_name['contents'].fields.append(
  _SYFTMESSAGE.fields_by_name['contents_delete_msg'])
_SYFTMESSAGE.fields_by_name['contents_delete_msg'].containing_oneof = _SYFTMESSAGE.oneofs_by_name['contents']
_SYFTMESSAGE.oneofs_by_name['contents'].fields.append(
  _SYFTMESSAGE.fields_by_name['contents_get_shape_msg'])
_SYFTMESSAGE.fields_by_name['contents_get_shape_msg'].containing_oneof = _SYFTMESSAGE.oneofs_by_name['contents']
_SYFTMESSAGE.oneofs_by_name['contents'].fields.append(
  _SYFTMESSAGE.fields_by_name['contents_is_none_msg'])
_SYFTMESSAGE.fields_by_name['contents_is_none_msg'].containing_oneof = _SYFTMESSAGE.oneofs_by_name['contents']
_SYFTMESSAGE.oneofs_by_name['contents'].fields.append(
  _SYFTMESSAGE.fields_by_name['contents_object_msg'])
_SYFTMESSAGE.fields_by_name['contents_object_msg'].containing_oneof = _SYFTMESSAGE.oneofs_by_name['contents']
_SYFTMESSAGE.oneofs_by_name['contents'].fields.append(
  _SYFTMESSAGE.fields_by_name['contents_object_request_msg'])
_SYFTMESSAGE.fields_by_name['contents_object_request_msg'].containing_oneof = _SYFTMESSAGE.oneofs_by_name['contents']
_SYFTMESSAGE.oneofs_by_name['contents'].fields.append(
  _SYFTMESSAGE.fields_by_name['contents_tensor_cmd_msg'])
_SYFTMESSAGE.fields_by_name['contents_tensor_cmd_msg'].containing_oneof = _SYFTMESSAGE.oneofs_by_name['contents']
_SYFTMESSAGE.oneofs_by_name['contents'].fields.append(
  _SYFTMESSAGE.fields_by_name['contents_plan_cmd_msg'])
_SYFTMESSAGE.fields_by_name['contents_plan_cmd_msg'].containing_oneof = _SYFTMESSAGE.oneofs_by_name['contents']
_SYFTMESSAGE.oneofs_by_name['contents'].fields.append(
  _SYFTMESSAGE.fields_by_name['contents_worker_cmd_msg'])
_SYFTMESSAGE.fields_by_name['contents_worker_cmd_msg'].containing_oneof = _SYFTMESSAGE.oneofs_by_name['contents']
_SYFTMESSAGE.oneofs_by_name['contents'].fields.append(
  _SYFTMESSAGE.fields_by_name['contents_search_msg'])
_SYFTMESSAGE.fields_by_name['contents_search_msg'].containing_oneof = _SYFTMESSAGE.oneofs_by_name['contents']
_ISNONEMESSAGE.fields_by_name['object_id'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
_OBJECTMESSAGE.fields_by_name['tensor'].message_type = syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__pb2._TORCHTENSOR
_TENSORCOMMANDMESSAGE.fields_by_name['computation'].message_type = syft__proto_dot_execution_dot_v1_dot_computation__action__pb2._COMPUTATIONACTION
_TENSORCOMMANDMESSAGE.fields_by_name['communication'].message_type = syft__proto_dot_execution_dot_v1_dot_communication__action__pb2._COMMUNICATIONACTION
_TENSORCOMMANDMESSAGE.oneofs_by_name['action'].fields.append(
  _TENSORCOMMANDMESSAGE.fields_by_name['computation'])
_TENSORCOMMANDMESSAGE.fields_by_name['computation'].containing_oneof = _TENSORCOMMANDMESSAGE.oneofs_by_name['action']
_TENSORCOMMANDMESSAGE.oneofs_by_name['action'].fields.append(
  _TENSORCOMMANDMESSAGE.fields_by_name['communication'])
_TENSORCOMMANDMESSAGE.fields_by_name['communication'].containing_oneof = _TENSORCOMMANDMESSAGE.oneofs_by_name['action']
_FORCEOBJECTDELETEMESSAGE.fields_by_name['object_ids'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
_GETSHAPEMESSAGE.fields_by_name['object_id'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
_OBJECTREQUESTMESSAGE.fields_by_name['object_id'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
_PLANCOMMANDMESSAGE.fields_by_name['args'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_arg__pb2._ARG
_WORKERCOMMANDMESSAGE.fields_by_name['args'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_arg__pb2._ARG
_SEARCHMESSAGE.fields_by_name['query'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
DESCRIPTOR.message_types_by_name['SyftMessage'] = _SYFTMESSAGE
DESCRIPTOR.message_types_by_name['IsNoneMessage'] = _ISNONEMESSAGE
DESCRIPTOR.message_types_by_name['ObjectMessage'] = _OBJECTMESSAGE
DESCRIPTOR.message_types_by_name['TensorCommandMessage'] = _TENSORCOMMANDMESSAGE
DESCRIPTOR.message_types_by_name['ForceObjectDeleteMessage'] = _FORCEOBJECTDELETEMESSAGE
DESCRIPTOR.message_types_by_name['GetShapeMessage'] = _GETSHAPEMESSAGE
DESCRIPTOR.message_types_by_name['ObjectRequestMessage'] = _OBJECTREQUESTMESSAGE
DESCRIPTOR.message_types_by_name['PlanCommandMessage'] = _PLANCOMMANDMESSAGE
DESCRIPTOR.message_types_by_name['WorkerCommandMessage'] = _WORKERCOMMANDMESSAGE
DESCRIPTOR.message_types_by_name['SearchMessage'] = _SEARCHMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SyftMessage = _reflection.GeneratedProtocolMessageType('SyftMessage', (_message.Message,), {
  'DESCRIPTOR' : _SYFTMESSAGE,
  '__module__' : 'syft_proto.messaging.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.messaging.v1.SyftMessage)
  })
_sym_db.RegisterMessage(SyftMessage)

IsNoneMessage = _reflection.GeneratedProtocolMessageType('IsNoneMessage', (_message.Message,), {
  'DESCRIPTOR' : _ISNONEMESSAGE,
  '__module__' : 'syft_proto.messaging.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.messaging.v1.IsNoneMessage)
  })
_sym_db.RegisterMessage(IsNoneMessage)

ObjectMessage = _reflection.GeneratedProtocolMessageType('ObjectMessage', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTMESSAGE,
  '__module__' : 'syft_proto.messaging.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.messaging.v1.ObjectMessage)
  })
_sym_db.RegisterMessage(ObjectMessage)

TensorCommandMessage = _reflection.GeneratedProtocolMessageType('TensorCommandMessage', (_message.Message,), {
  'DESCRIPTOR' : _TENSORCOMMANDMESSAGE,
  '__module__' : 'syft_proto.messaging.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.messaging.v1.TensorCommandMessage)
  })
_sym_db.RegisterMessage(TensorCommandMessage)

ForceObjectDeleteMessage = _reflection.GeneratedProtocolMessageType('ForceObjectDeleteMessage', (_message.Message,), {
  'DESCRIPTOR' : _FORCEOBJECTDELETEMESSAGE,
  '__module__' : 'syft_proto.messaging.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.messaging.v1.ForceObjectDeleteMessage)
  })
_sym_db.RegisterMessage(ForceObjectDeleteMessage)

GetShapeMessage = _reflection.GeneratedProtocolMessageType('GetShapeMessage', (_message.Message,), {
  'DESCRIPTOR' : _GETSHAPEMESSAGE,
  '__module__' : 'syft_proto.messaging.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.messaging.v1.GetShapeMessage)
  })
_sym_db.RegisterMessage(GetShapeMessage)

ObjectRequestMessage = _reflection.GeneratedProtocolMessageType('ObjectRequestMessage', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTREQUESTMESSAGE,
  '__module__' : 'syft_proto.messaging.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.messaging.v1.ObjectRequestMessage)
  })
_sym_db.RegisterMessage(ObjectRequestMessage)

PlanCommandMessage = _reflection.GeneratedProtocolMessageType('PlanCommandMessage', (_message.Message,), {
  'DESCRIPTOR' : _PLANCOMMANDMESSAGE,
  '__module__' : 'syft_proto.messaging.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.messaging.v1.PlanCommandMessage)
  })
_sym_db.RegisterMessage(PlanCommandMessage)

WorkerCommandMessage = _reflection.GeneratedProtocolMessageType('WorkerCommandMessage', (_message.Message,), {
  'DESCRIPTOR' : _WORKERCOMMANDMESSAGE,
  '__module__' : 'syft_proto.messaging.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.messaging.v1.WorkerCommandMessage)
  })
_sym_db.RegisterMessage(WorkerCommandMessage)

SearchMessage = _reflection.GeneratedProtocolMessageType('SearchMessage', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHMESSAGE,
  '__module__' : 'syft_proto.messaging.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.messaging.v1.SearchMessage)
  })
_sym_db.RegisterMessage(SearchMessage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)