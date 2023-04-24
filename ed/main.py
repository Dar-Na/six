# Import math Library
import math


def zawartosc_informacyjna(a, b):
    res = 0
    try:
        res = -1 * a / (a + b) * math.log2(a / (a + b)) - 1 * b / (a + b) * math.log2(b / (a + b))
    except:
        res = 0
    return res


def entropia(c, d, I_P_1, I_P_2):
    return c / (c + d) * I_P_1 + d / (c + d) * I_P_2


def entropia_mn(wsp, I_Ps):
    res = 0
    divider = 0
    for w in wsp:
        divider += w
    for i in range(len(wsp)):
        res += wsp[i] / divider * I_Ps[i]
    return res


def zysk_informacji(I_P, E_P):
    return I_P - E_P


def licz(arr):
    t_sum = 0
    n_sum = 0
    t_n = []
    I_Ps = []
    for i in range(len(arr)):
        t_sum += arr[i][0]
        n_sum += arr[i][1]
        I_Ps.append(zawartosc_informacyjna(arr[i][0], arr[i][1]))
        t_n.append(arr[i][0] + arr[i][1])
    # I_P_1 = zawartosc_informacyjna(t1, n1)
    # I_P_2 = zawartosc_informacyjna(t2, n2)
    # I_P_3 = zawartosc_informacyjna(t3, n3)
    print(I_Ps)
    I_P = zawartosc_informacyjna(t_sum, n_sum)
    # E_P = entropia(t1 + n1, t2 + n2, I_P_1, I_P_2)
    E_Pmn = entropia_mn(t_n, I_Ps)
    g_P = zysk_informacji(I_P, E_Pmn)
    for i in range(len(I_Ps)):
        print("I(P", i + 1, "): ", I_Ps[i])
    print("E(P): ", E_Pmn)
    print("g(P): ", g_P)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # t1, n1 = 2, 1
    # t2, n2 = 2, 2
    # t3, n3 = 0, 2
    # I_P = zawartosc_informacyjna(t1 + t2 + t3, n1 + n2 + n3)
    # I_P_1 = zawartosc_informacyjna(t1, n1)
    # I_P_2 = zawartosc_informacyjna(t2, n2)
    # I_P_3 = zawartosc_informacyjna(t3, n3)
    #
    # # E_P = entropia(t1 + n1, t2 + n2, I_P_1, I_P_2)
    # E_Pmn = entropia_mn([t1 + n1, t2 + n2, t3 + n3], [I_P_1, I_P_2, I_P_3])
    # g_P = zysk_informacji(I_P, E_Pmn)
    # print("I(P1): ", I_P_1)
    # print("I(P2): ", I_P_2)
    # print("I(P3): ", I_P_3)
    # print("E(P): ", E_Pmn)
    # print("g(P): ", g_P)

    licz([[2, 1], [2, 2], [0, 2]])
    licz([[3, 1], [1, 4]])
