# Deprecation note

This repository used to contain the [protocol buffer](https://developers.google.com/protocol-buffers) code that defined both the data model and [the exposition format](https://prometheus.io/docs/instrumenting/exposition_formats/#prometheus-protobuf-format) of Prometheus metrics. `client_model` was originally created because robust protobuf import tooling was non-existent at the time. Since then, tooling has improved (see [Buf](https://buf.build/)).

The generated Go code is still used in the [public, stable API of `client_golang`](https://github.com/prometheus/client_golang/blob/74560058a7af7a695db8196c8e84a0754032c6af/prometheus/metric.go#L54) until v2.

The source of truth for [the exposition format](https://prometheus.io/docs/instrumenting/exposition_formats/#prometheus-protobuf-format) has moved to [prometheus/prometheus](https://github.com/prometheus/prometheus/tree/main/prompb/io/prometheus/client) and is also available in the [Buf registry](https://buf.build/prometheus/prometheus/docs/main%3Aio.prometheus.client).

## History

Starting with v2.0.0, the [Prometheus server](https://github.com/prometheus/prometheus) stopped ingesting the protobuf-based exposition format. However, in v3.0.0 this restriction was lifted, and new features like native histograms were first introduced in the protobuf format. As of now, [the PrometheusProto exposition format](https://prometheus.io/docs/instrumenting/exposition_formats/#prometheus-protobuf-format) is an officially supported protocol that allows the community to experiment with new features.

## Recommended Usage & Buf Tooling

Formerly existing support for languages other than Go (namely C++, Java, Python, and Ruby) has been removed from this repository.

For new consumers and SDKs in other languages (such as Rust, C++, Java, Python, and Ruby), **we do not recommend manually copying proto files or depending on `client_model`**. Instead, the modern preferred solution is to use [Buf tooling](https://buf.build/) to generate bindings directly on the SDK side with specific language options, maintaining a clean dependency chain.

The centralized Prometheus protobuf definitions are available in the Buf registry, sourced directly from the main Prometheus repository:
[buf.build/prometheus/prometheus (io.prometheus.client)](https://buf.build/prometheus/prometheus/docs/main:io.prometheus.client)
