# Lambda
### There are four types of method references available.

-   Static method reference.
-   Instance Method (Bound receiver).
-   Instance Method (UnBound receiver).
-   Constructor reference.
1. Prefer lambdas to anonymous classes.



# Stream
### Use streams judiciously
1. Three primitive types are supported: int, long and double.
2. Stream pipelines are evaluated lazily: evaluation doesn’t start until the terminal operation is invoked, and data elements that aren’t required in order to complete the terminal operation are never computed. This lazy evaluation is what makes it possible to work with infinite streams. Note that a stream pipeline without a terminal operation is a silent no-op, so don’t forget to include one.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTcwNzU4NjY2NSwzMzUyNDExMDIsLTUyMz
YyMjE2NV19
-->