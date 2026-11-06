target = {12:110837, 24:245042, 36:407068, 48:602206, 60:836746,
          72:1118159, 84:1455325, 96:1858796, 108:2341109}

def sim(d, raise_rate, months, variant):
    """variant 'A': 先付利息再存钱; 'B': 先存钱再付利息"""
    s = 0.0
    out = {}
    cur_d = d
    for m in range(1, months + 1):
        if variant == 'A':
            s += s * 0.0225 / 12
            s += cur_d
        else:
            s += cur_d
            s += s * 0.0225 / 12
        if m % 6 == 0:
            cur_d *= (1 + raise_rate)
        if m % 12 == 0:
            out[m] = s
    return out

def match(variant, tol=1.0):
    hits = []
    for sal in range(40000, 600001, 1000):
        for port in range(1, 101):
            for rp in range(0, 16):
                d = sal / 12 * port / 100
                out = sim(d, rp / 100, 108, variant)
                if abs(out[12] - target[12]) <= tol and abs(out[24] - target[24]) <= tol \
                   and abs(out[108] - target[108]) <= tol:
                    hits.append((sal, port, rp, out))
    return hits

for v in ('A', 'B'):
    h = match(v)
    print(v, len(h))
    for x in h[:5]:
        print('  sal=%d port=%d raise=%d' % x[:3], {k: round(val) for k, val in x[3].items()})
