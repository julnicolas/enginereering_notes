package main

// This package shows how define structs with generics

import "fmt"

type Ptr32 uint32
type Ptr64 uint64

type Ptr[T Ptr32|Ptr64] struct {
	addr T
}

func (o *Ptr[T]) Get() T {
	return o.addr
}

func (o *Ptr[T]) Set(addr T) {
	o.addr = addr
}

func (o *Ptr[T]) Add(p *Ptr[T]) {
	o.addr += p.addr
}

func (o *Ptr[T]) String() string {
	return fmt.Sprintf("%T - 0x%x", o,o.addr)
}

// Use a named type constraint to mutualise type constraint definition
// type PtrT interface { Ptr32 | Ptr64 }
func NewPtr[T Ptr32|Ptr64](addr T) *Ptr[T] {
	p := &Ptr[T]{}
	p.Set(addr)

	return p
}

func main() {
	p32 := &Ptr[Ptr32]{}
	p32.Set(Ptr32(0xFFFFFFFF))
	p64 := &Ptr[Ptr64]{}
	p64.Set(Ptr64(0xFFFFFFFFFFFFFFFF))
	p := NewPtr(Ptr64(0xFFFFFFFFFFFFFFFF))

	// Build error - default is int, which is not a supported type
	//p2 := NewPtr(0xFFFFFFFFFFFFFFFF)

	fmt.Println(p32)
	fmt.Println(p64)
	fmt.Println(p)
}
