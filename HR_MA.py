#w_t=remtime d_h=remgreen w=rem m_L=carsout

M,N,T = map(int, input().split())
w_t = (T % 85)
if(w_t > 25):
    d_h = w_t - 25
else:
    d_h = 0
m_l = ( (T // 85) * 12 + d_h // 5)
w = (M + N + 1) - m_l
if(m_l >= M + 1):
    print(f"YES! {w}")
else:
    print(f"NO! {w}")