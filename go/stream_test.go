package model

import (
	"bytes"
	"encoding/binary"
	"reflect"
	"testing"

	"code.google.com/p/goprotobuf/proto"
)

func TestEncode(t *testing.T) {
	var (
		input = &Sample{Name: proto.String("counter"), Value: proto.Float64(10)}

		ref, _ = proto.Marshal(input)
		size   = uint64(len(ref))

		buf bytes.Buffer
		enc = NewEncoder(&buf)
	)

	if err := enc.Encode(input); err != nil {
		t.Fatal("unexpected error encoding sample:", err)
	}

	got, err := binary.ReadUvarint(&buf)
	if err != nil {
		t.Fatal("unexpected error reading size:", err)
	}

	if got != size {
		t.Fatalf("expected decoded size to be %d, was %d", size, got)
	}

	if !bytes.Equal(ref, buf.Bytes()) {
		t.Fatal("encoder output != proto.Marshal")
	}
}

func TestEncodeDecode(t *testing.T) {
	var (
		buf bytes.Buffer
		dec = NewDecoder(&buf)
		enc = NewEncoder(&buf)

		input = []*Sample{
			{Name: proto.String("counter"), Value: proto.Float64(10)},
			{Name: proto.String("gauge"), Value: proto.Float64(10), Time: proto.Int64(1390577363)},
		}
	)

	for i, s := range input {
		if err := enc.Encode(s); err != nil {
			t.Fatalf("%d. unexpected error encoding sample: %s", i, err)
		}

		got := &Sample{}

		if err := dec.Decode(got); err != nil {
			t.Fatalf("%d. unexpected error decoding sample: %s", i, err)
		}

		if !reflect.DeepEqual(s, got) {
			t.Fatalf("%d. %q != %q", i, s.String(), got.String())
		}
	}
}
