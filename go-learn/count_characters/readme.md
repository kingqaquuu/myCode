<!--
 * @Author: kingqaquuu
 * @Date: 2024-01-05 02:41:19
 * @FilePath: \myCode\go-learn\count_characters\readme.md
-->
## 创建一个用于统计字节和字符（rune）的程序，并对字符串 asSASA ddd dsjkdsjs dk 进行分析，然后再分析 asSASA ddd dsjkdsjsこん dk，最后解释两者不同的原因
RuneCountInString是统计unicode的字符数量,是个数
而len是用来直接用来统计所占字节,一般中文等特殊字符长度占3个字节