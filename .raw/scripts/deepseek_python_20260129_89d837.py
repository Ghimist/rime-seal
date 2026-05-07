with open('output.txt', 'w', encoding='utf-8') as f:
    for code in range(0x30000, 0x40000):
        try:
            f.write(f'U+{code:06X}: {chr(code)}\n')
        except:
            f.write(f'U+{code:06X}: [无法显示]\n')