import struct
import sys

def tile(r, c):
    return r * 16 + c

DIRT       = tile(0, 0)
TANK       = tile(13, 12)
FLAG       = tile(0, 4)
WATER      = tile(5, 0)
ANTITANK_U = tile(9, 0)
ANTITANK_R = tile(9, 4)
ANTITANK_D = tile(9, 8)
ANTITANK_L = tile(9, 12)
BLOCK      = tile(11, 4)
MOVE_BLOCK = tile(11, 8)
BRICKS     = tile(11, 12)
CRYSTAL    = tile(6, 0)
MIRROR_U   = tile(7, 0)
MIRROR_R   = tile(7, 4)
MIRROR_D   = tile(7, 8)
MIRROR_L   = tile(7, 12)
RMIRROR_U  = tile(8, 0)
RMIRROR_R  = tile(8, 4)
RMIRROR_D  = tile(8, 8)
RMIRROR_L  = tile(8, 12)
ONEWAY_U   = tile(1, 0)
ONEWAY_R   = tile(1, 4)
ONEWAY_D   = tile(1, 8)
ONEWAY_L   = tile(1, 12)
ICE        = tile(4, 0)
ICE_THIN   = tile(4, 4)
TUNNEL1    = tile(2, 0)
TUNNEL2    = tile(2, 4)
TUNNEL3    = tile(2, 8)
TUNNEL4    = tile(2, 12)
TUNNEL5    = tile(3, 0)
TUNNEL6    = tile(3, 4)
TUNNEL7    = tile(3, 8)
TUNNEL8    = tile(3, 12)

REMAP = {
     0: DIRT,
     1: TANK,
     2: FLAG,
     3: WATER,
     4: BLOCK,
     5: MOVE_BLOCK,
     6: BRICKS,
     7: ANTITANK_U,
     8: ANTITANK_R,
     9: ANTITANK_D,
    10: ANTITANK_L,
    11: MIRROR_U,
    12: MIRROR_R,
    13: MIRROR_D,
    14: MIRROR_L,
    15: ONEWAY_U,
    16: ONEWAY_R,
    17: ONEWAY_D,
    18: ONEWAY_L,
    19: CRYSTAL,
    20: RMIRROR_U,
    21: RMIRROR_R,
    22: RMIRROR_D,
    23: RMIRROR_L,
    24: ICE,
    25: ICE_THIN,
    64: TUNNEL1,
    65: TUNNEL1,
    66: TUNNEL2,
    67: TUNNEL2,
    68: TUNNEL3,
    69: TUNNEL3,
    70: TUNNEL4,
    71: TUNNEL4,
    72: TUNNEL5,
    73: TUNNEL5,
    74: TUNNEL6,
    75: TUNNEL6,
    76: TUNNEL7,
    77: TUNNEL7,
    78: TUNNEL8,
    79: TUNNEL8,
}

def remap(x):
    if x in REMAP:
        return REMAP[x]
    return 99

TRANS = str.maketrans({
    '"': '\\"',
    '\n': '\\n',
    '\x00': '',
    '\x01': '',
    '\x02': '',
    '\x03': '',
    '\x04': '',
    '\x05': '',
    '\x06': '',
    '\x07': '',
    '\x08': '',
    '\x09': '',
    '\x0b': '',
    '\x0c': '',
    '\x0d': '',
    '\x0e': '',
    '\x0f': '',
    '\x10': '',
    '\x11': '',
    '\x12': '',
    '\x13': '',
    '\x14': '',
    '\x15': '',
    '\x16': '',
    '\x17': '',
    '\x18': '',
    '\x19': '',
    '\x1a': '',
    '\x1b': '',
    '\x1c': '',
    '\x1d': '',
    '\x1e': '',
    '\x1f': ''
})

def format_str(b):
    s = b.decode('ascii', errors='backslashreplace')
    #s = b.decode('cp1252')
    s = s.translate(TRANS)
    return s

XADV = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    2,
    2,
    4,
    6,
    6,
    4,
    5,
    2,
    3,
    3,
    4,
    4,
    3,
    4,
    2,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    2,
    3,
    4,
    4,
    4,
    4,
    5,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    3,
    4,
    4,
    6,
    5,
    5,
    4,
    5,
    4,
    4,
    4,
    5,
    4,
    6,
    4,
    4,
    4,
    3,
    4,
    3,
    4,
    4,
    3,
    4,
    4,
    3,
    4,
    4,
    3,
    4,
    4,
    2,
    3,
    4,
    2,
    6,
    4,
    4,
    4,
    4,
    4,
    3,
    3,
    4,
    4,
    6,
    4,
    4,
    3,
    4,
    2,
    4,
    5,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    2,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1
]

def font_xadv(c):
    return XADV[ord(c)]

def wrap_str(s, w):
    s = list(s)
    
    for i in range(1, len(s)):
        if i + 1 < len(s) and s[i] == '\n' and s[i+1] != '\n' and s[i-1] != '\n':
            s[i] = ' '
        
    cw = 0
    i = 0
    ti = i
    tw = 0
    n = len(s)
    tn = n
    num_lines = 1
    while i < len(s) and tn != 0:
        c = s[i]
        if c == '\0': break
        i += 1
        tn -= 1
        cw += font_xadv(c)
        if c == '\n':
            cw = 0
            tw = 0
            ti = i
            num_lines += 1
        if c == ' ':
            ti = i
            tw = cw
            tn = n
        if cw <= w: continue
        if tw == 0: continue
        i = ti
        s[ti - 1] = '\n'
        num_lines += 1
        cw = 0
        tw = 0
        n = tn
    return (''.join(s), num_lines)

def format_hint(b):
    s = b.decode('ascii', errors='backslashreplace')
    s = s.translate(str.maketrans({ '\0': '', '\r': '' }))
    t = wrap_str(s, 128)
    if t[1] > 9:
        t = wrap_str(s, 120)
    s = t[0].translate(TRANS)
    return (s, t[1])

def convert(fin, sym):
    with open(fin, 'rb') as f:
        content = f.read()
    fout = '../src/levels/%s.abc' % sym.lower()
    with open(fout, 'w') as f:
        n = len(content) // 576
        f.write('level_t[%u] prog LEVELS_%s =\n{\n' % (n, sym))
        for i in range(n):
            d = content[i*576:(i+1)*576]
            tiles = d[:256]
            name = d[256:256+31]
            hint = d[256+31:256+31+256]
            author = d[256+31+256:256+31+256+31]
            diff = struct.unpack('H', d[-2:])
            f.write('    {\n')
            f.write('        {\n')
            for r in range(16):
                f.write('           ')
                for c in range(16):
                    f.write(' %3d,' % remap(tiles[c*16+r]))
                f.write('\n')
            f.write('        },\n')
            f.write('        "%s",\n' % format_str(name))
            f.write('        "%s",\n' % format_str(author))
            hint_info = format_hint(hint)
            f.write('        "%s",\n' % hint_info[0])
            f.write('        %u, %u,\n' % (hint_info[1], diff[0]))
            f.write('    },\n')
        f.write('};\n\n')

convert('ObjectsTutorial.lvl', 'TUTORIAL_OBJECTS')
convert('Tutor-with-Playbacks.lvl', 'TUTORIAL_BEGINNER')
convert('Tutor.lvl', 'TUTORIAL_TRICKS')
convert('LaserTank.lvl', 'STANDARD')
