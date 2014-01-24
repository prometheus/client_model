package model

import (
	"bufio"
	"bytes"
	"encoding/binary"
	"io"

	"code.google.com/p/goprotobuf/proto"
)

// MarshalError wraps errors generated while marshaling a protobuf message.
type MarshalError struct {
	Err error
}

func (e MarshalError) Error() string { return e.Err.Error() }

// Encoder writes varint-encoded length-delimited protobuf messages to
// an output stream.
type Encoder struct {
	w       io.Writer
	buf     *proto.Buffer
	sizeBuf []byte
	err     error
}

// NewEncoder returns a new Encoder that writes to w.
func NewEncoder(w io.Writer) *Encoder {
	return &Encoder{
		w:       w,
		buf:     new(proto.Buffer),
		sizeBuf: make([]byte, binary.MaxVarintLen32),
	}
}

// Encode writes the varint-encoded length-delimited protobuf encoding of pb to
// the stream.
//
// If Encode returns a MarshalError, the Encoder and its stream can still be
// used.
func (enc *Encoder) Encode(pb proto.Message) error {
	if enc.err != nil {
		return enc.err
	}

	defer enc.buf.Reset()

	if err := enc.buf.Marshal(pb); err != nil {
		return MarshalError{err}
	}

	var (
		message = enc.buf.Bytes()
		end     = binary.PutUvarint(enc.sizeBuf, uint64(len(message)))
		size    = enc.sizeBuf[:end]
	)

	if _, err := enc.w.Write(size); err != nil {
		enc.err = err
		return err
	}

	if _, err := enc.w.Write(message); err != nil {
		enc.err = err
		return err
	}

	return nil
}

// A Decoder reads varint-encoded length-delimited protobuf messages from an
// input stream.
type Decoder struct {
	r   *bufio.Reader
	buf *bytes.Buffer
	err error
}

// NewDecoder returns a new Decoder that reads from r.
func NewDecoder(r io.Reader) *Decoder {
	return &Decoder{
		r:   bufio.NewReader(r),
		buf: new(bytes.Buffer),
	}
}

// Decoder reads the next message from its input and stores it in the value
// pointed to by pb.
func (dec *Decoder) Decode(pb proto.Message) error {
	if dec.err != nil {
		return dec.err
	}

	size, err := binary.ReadUvarint(dec.r)

	if err != nil {
		dec.err = err
		return err
	}

	defer dec.buf.Reset()

	if _, err := io.CopyN(dec.buf, dec.r, int64(size)); err != nil {
		dec.err = err
		return err
	}

	if err := proto.Unmarshal(dec.buf.Bytes(), pb); err != nil {
		dec.err = err
		return err
	}

	return nil
}
