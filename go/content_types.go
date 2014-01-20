package model

import (
	"mime"
)

var (
	SampleContentType = mime.FormatMediaType(
		"application/vnd.google.protobuf", map[string]string{
			"proto":    "io.prometheus.client.Sample",
			"encoding": "delimited",
		},
	)

	MetricFamilyContentType = mime.FormatMediaType(
		"application/vnd.google.protobuf", map[string]string{
			"proto":    "io.prometheus.client.MetricFamily",
			"encoding": "delimited",
		},
	)
)
