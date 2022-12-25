## Tại sao boolean value chỉ cần 1 bit giá trị để lưu true/false (1/0) mà cần tận tới 1byte?
- Đầu tiên, cần phân tích virtual address memory: Khi một ứng dụng chạy trên OS [32-bit](https://en.wikipedia.org/wiki/32-bit "32-bit"). Và proces có 4Gib VAS(virtual address space) => virtual address space sẽ rơi vào từ.  $0 \from 2^{32} - 1$(from 0 to 232 − 1) in that space can have a single byte as a value. Initially, none of them have values ('-' represents no value). Using or setting values in such a VAS would cause a [memory exception](https://en.wikipedia.org/wiki/Page_fault "Page fault").
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzI1ODYzNzYzLDczMDk5ODExNl19
-->