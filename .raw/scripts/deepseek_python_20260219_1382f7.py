#!/usr/bin/env python3
start = 0x3f817
end = 0x3fc3f  # 注意Python的range是半开，不包括end
for code in range(start, end):
    print(chr(code) + '\t')