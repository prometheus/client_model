# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='metrics.proto',
  package='io.prometheus.client',
  serialized_pb='\n\rmetrics.proto\x12\x14io.prometheus.client\"(\n\tLabelPair\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x16\n\x05Gauge\x12\r\n\x05value\x18\x01 \x01(\x01\"\x18\n\x07\x43ounter\x12\r\n\x05value\x18\x01 \x01(\x01\"+\n\x08Quantile\x12\x10\n\x08quantile\x18\x01 \x01(\x01\x12\r\n\x05value\x18\x02 \x01(\x01\"e\n\x07Summary\x12\x14\n\x0csample_count\x18\x01 \x01(\x04\x12\x12\n\nsample_sum\x18\x02 \x01(\x01\x12\x30\n\x08quantile\x18\x03 \x03(\x0b\x32\x1e.io.prometheus.client.Quantile\"\x17\n\x06\x43ustom\x12\r\n\x05value\x18\x01 \x01(\x01\"\x88\x02\n\x06Metric\x12.\n\x05label\x18\x01 \x03(\x0b\x32\x1f.io.prometheus.client.LabelPair\x12*\n\x05gauge\x18\x02 \x01(\x0b\x32\x1b.io.prometheus.client.Gauge\x12.\n\x07\x63ounter\x18\x03 \x01(\x0b\x32\x1d.io.prometheus.client.Counter\x12.\n\x07summary\x18\x04 \x01(\x0b\x32\x1d.io.prometheus.client.Summary\x12,\n\x06\x63ustom\x18\x05 \x01(\x0b\x32\x1c.io.prometheus.client.Custom\x12\x14\n\x0ctimestamp_ms\x18\x06 \x01(\x03\"\x88\x01\n\x0cMetricFamily\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04help\x18\x02 \x01(\t\x12.\n\x04type\x18\x03 \x01(\x0e\x32 .io.prometheus.client.MetricType\x12,\n\x06metric\x18\x04 \x03(\x0b\x32\x1c.io.prometheus.client.Metric*1\n\nMetricType\x12\x0b\n\x07\x43OUNTER\x10\x00\x12\t\n\x05GAUGE\x10\x01\x12\x0b\n\x07SUMMARY\x10\x02\x42\x16\n\x14io.prometheus.client')

_METRICTYPE = descriptor.EnumDescriptor(
  name='MetricType',
  full_name='io.prometheus.client.MetricType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='COUNTER', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='GAUGE', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SUMMARY', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=710,
  serialized_end=759,
)


COUNTER = 0
GAUGE = 1
SUMMARY = 2



_LABELPAIR = descriptor.Descriptor(
  name='LabelPair',
  full_name='io.prometheus.client.LabelPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='io.prometheus.client.LabelPair.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='io.prometheus.client.LabelPair.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=39,
  serialized_end=79,
)


_GAUGE = descriptor.Descriptor(
  name='Gauge',
  full_name='io.prometheus.client.Gauge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='value', full_name='io.prometheus.client.Gauge.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
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
  extension_ranges=[],
  serialized_start=81,
  serialized_end=103,
)


_COUNTER = descriptor.Descriptor(
  name='Counter',
  full_name='io.prometheus.client.Counter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='value', full_name='io.prometheus.client.Counter.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
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
  extension_ranges=[],
  serialized_start=105,
  serialized_end=129,
)


_QUANTILE = descriptor.Descriptor(
  name='Quantile',
  full_name='io.prometheus.client.Quantile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='quantile', full_name='io.prometheus.client.Quantile.quantile', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='io.prometheus.client.Quantile.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  extension_ranges=[],
  serialized_start=131,
  serialized_end=174,
)


_SUMMARY = descriptor.Descriptor(
  name='Summary',
  full_name='io.prometheus.client.Summary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sample_count', full_name='io.prometheus.client.Summary.sample_count', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sample_sum', full_name='io.prometheus.client.Summary.sample_sum', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='quantile', full_name='io.prometheus.client.Summary.quantile', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=176,
  serialized_end=277,
)


_CUSTOM = descriptor.Descriptor(
  name='Custom',
  full_name='io.prometheus.client.Custom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='value', full_name='io.prometheus.client.Custom.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
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
  extension_ranges=[],
  serialized_start=279,
  serialized_end=302,
)


_METRIC = descriptor.Descriptor(
  name='Metric',
  full_name='io.prometheus.client.Metric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='label', full_name='io.prometheus.client.Metric.label', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gauge', full_name='io.prometheus.client.Metric.gauge', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='counter', full_name='io.prometheus.client.Metric.counter', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='summary', full_name='io.prometheus.client.Metric.summary', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='custom', full_name='io.prometheus.client.Metric.custom', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timestamp_ms', full_name='io.prometheus.client.Metric.timestamp_ms', index=5,
      number=6, type=3, cpp_type=2, label=1,
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
  extension_ranges=[],
  serialized_start=305,
  serialized_end=569,
)


_METRICFAMILY = descriptor.Descriptor(
  name='MetricFamily',
  full_name='io.prometheus.client.MetricFamily',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='io.prometheus.client.MetricFamily.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='help', full_name='io.prometheus.client.MetricFamily.help', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='io.prometheus.client.MetricFamily.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='metric', full_name='io.prometheus.client.MetricFamily.metric', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=572,
  serialized_end=708,
)

_SUMMARY.fields_by_name['quantile'].message_type = _QUANTILE
_METRIC.fields_by_name['label'].message_type = _LABELPAIR
_METRIC.fields_by_name['gauge'].message_type = _GAUGE
_METRIC.fields_by_name['counter'].message_type = _COUNTER
_METRIC.fields_by_name['summary'].message_type = _SUMMARY
_METRIC.fields_by_name['custom'].message_type = _CUSTOM
_METRICFAMILY.fields_by_name['type'].enum_type = _METRICTYPE
_METRICFAMILY.fields_by_name['metric'].message_type = _METRIC
DESCRIPTOR.message_types_by_name['LabelPair'] = _LABELPAIR
DESCRIPTOR.message_types_by_name['Gauge'] = _GAUGE
DESCRIPTOR.message_types_by_name['Counter'] = _COUNTER
DESCRIPTOR.message_types_by_name['Quantile'] = _QUANTILE
DESCRIPTOR.message_types_by_name['Summary'] = _SUMMARY
DESCRIPTOR.message_types_by_name['Custom'] = _CUSTOM
DESCRIPTOR.message_types_by_name['Metric'] = _METRIC
DESCRIPTOR.message_types_by_name['MetricFamily'] = _METRICFAMILY

class LabelPair(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LABELPAIR
  
  # @@protoc_insertion_point(class_scope:io.prometheus.client.LabelPair)

class Gauge(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GAUGE
  
  # @@protoc_insertion_point(class_scope:io.prometheus.client.Gauge)

class Counter(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COUNTER
  
  # @@protoc_insertion_point(class_scope:io.prometheus.client.Counter)

class Quantile(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUANTILE
  
  # @@protoc_insertion_point(class_scope:io.prometheus.client.Quantile)

class Summary(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUMMARY
  
  # @@protoc_insertion_point(class_scope:io.prometheus.client.Summary)

class Custom(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CUSTOM
  
  # @@protoc_insertion_point(class_scope:io.prometheus.client.Custom)

class Metric(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _METRIC
  
  # @@protoc_insertion_point(class_scope:io.prometheus.client.Metric)

class MetricFamily(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _METRICFAMILY
  
  # @@protoc_insertion_point(class_scope:io.prometheus.client.MetricFamily)

# @@protoc_insertion_point(module_scope)