package simplefactory

import "testing"

func TestSimpleFactory(t *testing.T) {
	cat := NewSimpleApi("cat")
	if cat.Sing() != "cat" {
		t.Fatal("cat type failed!")
	}

	dog := NewSimpleApi("dog")
	if dog.Sing() != "dog" {
		t.Fatal("dog type failed!")
	}
}
