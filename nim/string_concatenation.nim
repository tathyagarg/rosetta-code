import std/strformat

var
  a = "Hello, "
  b = "world!"

echo fmt"a = '{a}', b = '{b}'"

var c = a & b
echo fmt"c = '{c}'"
