第一个只出现一次的字符

在一个字符串中找到第一个只出现一次的字符。如输入abaccdeff，则输出b
接替思路
遇到题目中明确指出“字符串”的问题，可以考虑：是否可以申请int a[256]的一个数组，采取“直接Hash”模式：将字符值直接映射成数组索引。本题目中，恰好可以这么处理。算法开始，将a数组的元素都初始化为0；然后遍历字符串，将a[str[i]] ，完成每个字符的计数；最后再遍历一遍字符串，第一个满足a[str[i]]==1，则str[i]即为所求。
