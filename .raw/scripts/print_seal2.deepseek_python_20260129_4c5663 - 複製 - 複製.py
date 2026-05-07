import os, sys
name = os.path.splitext(os.path.basename(sys.argv[0]))[0] + ".txt"
with open(name, 'w', encoding='utf-8') as f:
    for i, code in enumerate(range(0x3f817, 0x3FC40)):
        try: f.write(chr(code))
        except: f.write(' ')
        if (i + 1) % 16 == 0: f.write('\n')
        if (i + 1) % 256 == 0: f.write('\n')
print(f"已保存到: {name}")