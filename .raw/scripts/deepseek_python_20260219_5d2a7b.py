#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

def main():
    # 获取当前脚本的文件名（不含扩展名）
    script_name = os.path.splitext(os.path.basename(__file__))[0]
    output_filename = script_name + ".md"
    
    # 设置码点范围（包含结束值）
    start = 0x3D000
    end = 0x3FC3F
    total = end - start + 1  # 11328
    print(f"将输出 {total} 个字符到文件 {output_filename}")
    
    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            for code in range(start, end + 1):
                try:
                    ch = chr(code)  # 将码点转换为字符
                    # 格式：16进制码位(大写) + tab + 字符 + tab + 换行
                    f.write(f"{code:06X}\t{ch}\t\n")
                except ValueError:
                    # 极少数无效码点时的后备（此范围内理论上不会出现）
                    f.write(f"{code:06X}\t[INVALID]\t\n")
        print("完成！")
    except Exception as e:
        print(f"写入文件时出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()