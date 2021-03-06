# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lolserverprotocol/lolapi.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lolserverprotocol/lolapi.proto',
  package='LoLAPIProtocol',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1elolserverprotocol/lolapi.proto\x12\x0eLoLAPIProtocol\"\xfa\x02\n\x07Request\x12:\n\x0c\x63lients_join\x18\x01 \x01(\x0b\x32\".LoLAPIProtocol.RequestClientsJoinH\x00\x12:\n\x0cgame_started\x18\x02 \x01(\x0b\x32\".LoLAPIProtocol.RequestGameStartedH\x00\x12@\n\x0fstart_observing\x18\x03 \x01(\x0b\x32%.LoLAPIProtocol.RequestStartObservingH\x00\x12\x39\n\x0bobservation\x18\x04 \x01(\x0b\x32\".LoLAPIProtocol.RequestObservationH\x00\x12/\n\x06\x61\x63tion\x18\x05 \x01(\x0b\x32\x1d.LoLAPIProtocol.RequestActionH\x00\x12>\n\x0e\x62roadcast_chat\x18\x06 \x01(\x0b\x32$.LoLAPIProtocol.RequestBroadcastChatH\x00\x42\t\n\x07request\"\x82\x03\n\x08Response\x12;\n\x0c\x63lients_join\x18\x01 \x01(\x0b\x32#.LoLAPIProtocol.ResponseClientsJoinH\x00\x12;\n\x0cgame_started\x18\x02 \x01(\x0b\x32#.LoLAPIProtocol.ResponseGameStartedH\x00\x12\x41\n\x0fstart_observing\x18\x03 \x01(\x0b\x32&.LoLAPIProtocol.ResponseStartObservingH\x00\x12:\n\x0bobservation\x18\x04 \x01(\x0b\x32#.LoLAPIProtocol.ResponseObservationH\x00\x12\x30\n\x06\x61\x63tion\x18\x05 \x01(\x0b\x32\x1e.LoLAPIProtocol.ResponseActionH\x00\x12?\n\x0e\x62roadcast_chat\x18\x06 \x01(\x0b\x32%.LoLAPIProtocol.ResponseBroadcastChatH\x00\x42\n\n\x08response\"\x14\n\x12RequestClientsJoin\"\x15\n\x13ResponseClientsJoin\"\x14\n\x12RequestGameStarted\"\x15\n\x13ResponseGameStarted\"\x17\n\x15RequestStartObserving\"\x18\n\x16ResponseStartObserving\"\x14\n\x12RequestObservation\"H\n\x13ResponseObservation\x12\x31\n\x0cobservations\x18\x01 \x03(\x0b\x32\x1b.LoLAPIProtocol.Observation\"8\n\rRequestAction\x12\'\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32\x16.LoLAPIProtocol.Action\"\x10\n\x0eResponseAction\"\'\n\x14RequestBroadcastChat\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x17\n\x15ResponseBroadcastChat\"\"\n\x0bObservation\x12\x13\n\x0bobservation\x18\x01 \x01(\t\"\x18\n\x06\x41\x63tion\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='LoLAPIProtocol.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clients_join', full_name='LoLAPIProtocol.Request.clients_join', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_started', full_name='LoLAPIProtocol.Request.game_started', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_observing', full_name='LoLAPIProtocol.Request.start_observing', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observation', full_name='LoLAPIProtocol.Request.observation', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='LoLAPIProtocol.Request.action', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='broadcast_chat', full_name='LoLAPIProtocol.Request.broadcast_chat', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='request', full_name='LoLAPIProtocol.Request.request',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=51,
  serialized_end=429,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='LoLAPIProtocol.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clients_join', full_name='LoLAPIProtocol.Response.clients_join', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_started', full_name='LoLAPIProtocol.Response.game_started', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_observing', full_name='LoLAPIProtocol.Response.start_observing', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observation', full_name='LoLAPIProtocol.Response.observation', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='LoLAPIProtocol.Response.action', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='broadcast_chat', full_name='LoLAPIProtocol.Response.broadcast_chat', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='response', full_name='LoLAPIProtocol.Response.response',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=432,
  serialized_end=818,
)


_REQUESTCLIENTSJOIN = _descriptor.Descriptor(
  name='RequestClientsJoin',
  full_name='LoLAPIProtocol.RequestClientsJoin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=820,
  serialized_end=840,
)


_RESPONSECLIENTSJOIN = _descriptor.Descriptor(
  name='ResponseClientsJoin',
  full_name='LoLAPIProtocol.ResponseClientsJoin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=842,
  serialized_end=863,
)


_REQUESTGAMESTARTED = _descriptor.Descriptor(
  name='RequestGameStarted',
  full_name='LoLAPIProtocol.RequestGameStarted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=865,
  serialized_end=885,
)


_RESPONSEGAMESTARTED = _descriptor.Descriptor(
  name='ResponseGameStarted',
  full_name='LoLAPIProtocol.ResponseGameStarted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=887,
  serialized_end=908,
)


_REQUESTSTARTOBSERVING = _descriptor.Descriptor(
  name='RequestStartObserving',
  full_name='LoLAPIProtocol.RequestStartObserving',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=910,
  serialized_end=933,
)


_RESPONSESTARTOBSERVING = _descriptor.Descriptor(
  name='ResponseStartObserving',
  full_name='LoLAPIProtocol.ResponseStartObserving',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=935,
  serialized_end=959,
)


_REQUESTOBSERVATION = _descriptor.Descriptor(
  name='RequestObservation',
  full_name='LoLAPIProtocol.RequestObservation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=961,
  serialized_end=981,
)


_RESPONSEOBSERVATION = _descriptor.Descriptor(
  name='ResponseObservation',
  full_name='LoLAPIProtocol.ResponseObservation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observations', full_name='LoLAPIProtocol.ResponseObservation.observations', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=983,
  serialized_end=1055,
)


_REQUESTACTION = _descriptor.Descriptor(
  name='RequestAction',
  full_name='LoLAPIProtocol.RequestAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actions', full_name='LoLAPIProtocol.RequestAction.actions', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1057,
  serialized_end=1113,
)


_RESPONSEACTION = _descriptor.Descriptor(
  name='ResponseAction',
  full_name='LoLAPIProtocol.ResponseAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1115,
  serialized_end=1131,
)


_REQUESTBROADCASTCHAT = _descriptor.Descriptor(
  name='RequestBroadcastChat',
  full_name='LoLAPIProtocol.RequestBroadcastChat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='LoLAPIProtocol.RequestBroadcastChat.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1133,
  serialized_end=1172,
)


_RESPONSEBROADCASTCHAT = _descriptor.Descriptor(
  name='ResponseBroadcastChat',
  full_name='LoLAPIProtocol.ResponseBroadcastChat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1174,
  serialized_end=1197,
)


_OBSERVATION = _descriptor.Descriptor(
  name='Observation',
  full_name='LoLAPIProtocol.Observation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observation', full_name='LoLAPIProtocol.Observation.observation', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1199,
  serialized_end=1233,
)


_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='LoLAPIProtocol.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='LoLAPIProtocol.Action.action', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1235,
  serialized_end=1259,
)

_REQUEST.fields_by_name['clients_join'].message_type = _REQUESTCLIENTSJOIN
_REQUEST.fields_by_name['game_started'].message_type = _REQUESTGAMESTARTED
_REQUEST.fields_by_name['start_observing'].message_type = _REQUESTSTARTOBSERVING
_REQUEST.fields_by_name['observation'].message_type = _REQUESTOBSERVATION
_REQUEST.fields_by_name['action'].message_type = _REQUESTACTION
_REQUEST.fields_by_name['broadcast_chat'].message_type = _REQUESTBROADCASTCHAT
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['clients_join'])
_REQUEST.fields_by_name['clients_join'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['game_started'])
_REQUEST.fields_by_name['game_started'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['start_observing'])
_REQUEST.fields_by_name['start_observing'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['observation'])
_REQUEST.fields_by_name['observation'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['action'])
_REQUEST.fields_by_name['action'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['broadcast_chat'])
_REQUEST.fields_by_name['broadcast_chat'].containing_oneof = _REQUEST.oneofs_by_name['request']
_RESPONSE.fields_by_name['clients_join'].message_type = _RESPONSECLIENTSJOIN
_RESPONSE.fields_by_name['game_started'].message_type = _RESPONSEGAMESTARTED
_RESPONSE.fields_by_name['start_observing'].message_type = _RESPONSESTARTOBSERVING
_RESPONSE.fields_by_name['observation'].message_type = _RESPONSEOBSERVATION
_RESPONSE.fields_by_name['action'].message_type = _RESPONSEACTION
_RESPONSE.fields_by_name['broadcast_chat'].message_type = _RESPONSEBROADCASTCHAT
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['clients_join'])
_RESPONSE.fields_by_name['clients_join'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['game_started'])
_RESPONSE.fields_by_name['game_started'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['start_observing'])
_RESPONSE.fields_by_name['start_observing'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['observation'])
_RESPONSE.fields_by_name['observation'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['action'])
_RESPONSE.fields_by_name['action'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['broadcast_chat'])
_RESPONSE.fields_by_name['broadcast_chat'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSEOBSERVATION.fields_by_name['observations'].message_type = _OBSERVATION
_REQUESTACTION.fields_by_name['actions'].message_type = _ACTION
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['RequestClientsJoin'] = _REQUESTCLIENTSJOIN
DESCRIPTOR.message_types_by_name['ResponseClientsJoin'] = _RESPONSECLIENTSJOIN
DESCRIPTOR.message_types_by_name['RequestGameStarted'] = _REQUESTGAMESTARTED
DESCRIPTOR.message_types_by_name['ResponseGameStarted'] = _RESPONSEGAMESTARTED
DESCRIPTOR.message_types_by_name['RequestStartObserving'] = _REQUESTSTARTOBSERVING
DESCRIPTOR.message_types_by_name['ResponseStartObserving'] = _RESPONSESTARTOBSERVING
DESCRIPTOR.message_types_by_name['RequestObservation'] = _REQUESTOBSERVATION
DESCRIPTOR.message_types_by_name['ResponseObservation'] = _RESPONSEOBSERVATION
DESCRIPTOR.message_types_by_name['RequestAction'] = _REQUESTACTION
DESCRIPTOR.message_types_by_name['ResponseAction'] = _RESPONSEACTION
DESCRIPTOR.message_types_by_name['RequestBroadcastChat'] = _REQUESTBROADCASTCHAT
DESCRIPTOR.message_types_by_name['ResponseBroadcastChat'] = _RESPONSEBROADCASTCHAT
DESCRIPTOR.message_types_by_name['Observation'] = _OBSERVATION
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'lolserverprotocol.lolapi_pb2'
  # @@protoc_insertion_point(class_scope:LoLAPIProtocol.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'lolserverprotocol.lolapi_pb2'
  # @@protoc_insertion_point(class_scope:LoLAPIProtocol.Response)
  ))
_sym_db.RegisterMessage(Response)

RequestClientsJoin = _reflection.GeneratedProtocolMessageType('RequestClientsJoin', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTCLIENTSJOIN,
  __module__ = 'lolserverprotocol.lolapi_pb2'
  # @@protoc_insertion_point(class_scope:LoLAPIProtocol.RequestClientsJoin)
  ))
_sym_db.RegisterMessage(RequestClientsJoin)

ResponseClientsJoin = _reflection.GeneratedProtocolMessageType('ResponseClientsJoin', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSECLIENTSJOIN,
  __module__ = 'lolserverprotocol.lolapi_pb2'
  # @@protoc_insertion_point(class_scope:LoLAPIProtocol.ResponseClientsJoin)
  ))
_sym_db.RegisterMessage(ResponseClientsJoin)

RequestGameStarted = _reflection.GeneratedProtocolMessageType('RequestGameStarted', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTGAMESTARTED,
  __module__ = 'lolserverprotocol.lolapi_pb2'
  # @@protoc_insertion_point(class_scope:LoLAPIProtocol.RequestGameStarted)
  ))
_sym_db.RegisterMessage(RequestGameStarted)

ResponseGameStarted = _reflection.GeneratedProtocolMessageType('ResponseGameStarted', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEGAMESTARTED,
  __module__ = 'lolserverprotocol.lolapi_pb2'
  # @@protoc_insertion_point(class_scope:LoLAPIProtocol.ResponseGameStarted)
  ))
_sym_db.RegisterMessage(ResponseGameStarted)

RequestStartObserving = _reflection.GeneratedProtocolMessageType('RequestStartObserving', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTSTARTOBSERVING,
  __module__ = 'lolserverprotocol.lolapi_pb2'
  # @@protoc_insertion_point(class_scope:LoLAPIProtocol.RequestStartObserving)
  ))
_sym_db.RegisterMessage(RequestStartObserving)

ResponseStartObserving = _reflection.GeneratedProtocolMessageType('ResponseStartObserving', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSESTARTOBSERVING,
  __module__ = 'lolserverprotocol.lolapi_pb2'
  # @@protoc_insertion_point(class_scope:LoLAPIProtocol.ResponseStartObserving)
  ))
_sym_db.RegisterMessage(ResponseStartObserving)

RequestObservation = _reflection.GeneratedProtocolMessageType('RequestObservation', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTOBSERVATION,
  __module__ = 'lolserverprotocol.lolapi_pb2'
  # @@protoc_insertion_point(class_scope:LoLAPIProtocol.RequestObservation)
  ))
_sym_db.RegisterMessage(RequestObservation)

ResponseObservation = _reflection.GeneratedProtocolMessageType('ResponseObservation', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEOBSERVATION,
  __module__ = 'lolserverprotocol.lolapi_pb2'
  # @@protoc_insertion_point(class_scope:LoLAPIProtocol.ResponseObservation)
  ))
_sym_db.RegisterMessage(ResponseObservation)

RequestAction = _reflection.GeneratedProtocolMessageType('RequestAction', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTACTION,
  __module__ = 'lolserverprotocol.lolapi_pb2'
  # @@protoc_insertion_point(class_scope:LoLAPIProtocol.RequestAction)
  ))
_sym_db.RegisterMessage(RequestAction)

ResponseAction = _reflection.GeneratedProtocolMessageType('ResponseAction', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEACTION,
  __module__ = 'lolserverprotocol.lolapi_pb2'
  # @@protoc_insertion_point(class_scope:LoLAPIProtocol.ResponseAction)
  ))
_sym_db.RegisterMessage(ResponseAction)

RequestBroadcastChat = _reflection.GeneratedProtocolMessageType('RequestBroadcastChat', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTBROADCASTCHAT,
  __module__ = 'lolserverprotocol.lolapi_pb2'
  # @@protoc_insertion_point(class_scope:LoLAPIProtocol.RequestBroadcastChat)
  ))
_sym_db.RegisterMessage(RequestBroadcastChat)

ResponseBroadcastChat = _reflection.GeneratedProtocolMessageType('ResponseBroadcastChat', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEBROADCASTCHAT,
  __module__ = 'lolserverprotocol.lolapi_pb2'
  # @@protoc_insertion_point(class_scope:LoLAPIProtocol.ResponseBroadcastChat)
  ))
_sym_db.RegisterMessage(ResponseBroadcastChat)

Observation = _reflection.GeneratedProtocolMessageType('Observation', (_message.Message,), dict(
  DESCRIPTOR = _OBSERVATION,
  __module__ = 'lolserverprotocol.lolapi_pb2'
  # @@protoc_insertion_point(class_scope:LoLAPIProtocol.Observation)
  ))
_sym_db.RegisterMessage(Observation)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), dict(
  DESCRIPTOR = _ACTION,
  __module__ = 'lolserverprotocol.lolapi_pb2'
  # @@protoc_insertion_point(class_scope:LoLAPIProtocol.Action)
  ))
_sym_db.RegisterMessage(Action)


# @@protoc_insertion_point(module_scope)
