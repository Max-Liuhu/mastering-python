1. array: 定长，操作有限，但是节省内存

2. list: 会预先分配内存，操作丰富，但是耗费内存

```
list.append: 如果之前没有分配够内存，会重新开辟新区域，然后复制之前的数据，复杂度退化
list.insert: 会移动被插入区域后所有元素,O(n)
list.pop: pop不同位置需要的复杂度不同pop(0)是O(1)复杂度,pop()首位O(n)复杂度
list[]: slice操作copy数据（预留空间）到另一个list
```
