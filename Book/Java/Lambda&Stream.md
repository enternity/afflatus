# Lambda
### There are four types of method references available.

1.  Static method reference.
2.  Instance Method (Bound receiver).
3.  Instance Method (UnBound receiver).
4.  Constructor reference.
# Stream
### Use streams judiciously
1. Three primitive types are supported: int, long and double.
2. Stream pipelines are evaluated lazily: evaluation doesn’t start until the terminal operation is invoked, and data elements that aren’t required in order to complete the terminal operation are never computed. This lazy evaluation is what makes it possible to work with infinite streams. Note that a stream pipeline without a terminal operation is a silent no-op, so don’t forget to include one.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzM1MjQxMTAyLC01MjM2MjIxNjVdfQ==
-->