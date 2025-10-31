from operator import itemgetter
import re


def load(filename):

    with open(filename) as f:
        data = f.read().strip()

    machines = data.split("\n\n")
    configs = []
    bap = re.compile(r"\d+")

    for m in machines:
        ba, bb, prize = m.splitlines()
        bax, bay = re.findall(bap, ba)
        a_config = (int(bax), int(bay))

        bax, bay = re.findall(bap, bb)
        b_config = (int(bax), int(bay))

        pax, pay = re.findall(bap, prize)
        p_config = (int(pax), int(pay))

        configs.append((a_config, b_config, p_config))

    return configs


# def p1(configs):
#     cost_a = 3
#     cost_b = 1

#     m_costs = []
#     max_press_a = 100
#     max_press_b = 100
#     for machine in configs:
#         ba, bb, prize = machine
#         px, py = prize
#         bax, bay = ba
#         bbx, bby = bb

#         press_b = min(px // bbx, max_press_b)
#         press_a = min(px // bax, max_press_a)
#         combos = []
#         for i in range(press_b + 1):
#             for j in range(press_a + 1):
#                 combos.append((i, j))

#         combos = sorted(combos, key=itemgetter(1, 0), reverse=True)
#         cost = -1
#         for n_press_b, n_press_a in combos:
#             if (n_press_b * bbx + n_press_a * bax == px) and (
#                 n_press_b * bby + n_press_a * bay == py
#             ):
#                 cost = cost_b * n_press_b + cost_a * n_press_a
#                 break
#         m_costs.append(cost)


#     print(m_costs)
#     total_cost = sum(c for c in m_costs if c != -1)
#     return total_cost


def p1(configs):
    cost_a = 3
    cost_b = 1

    m_costs = []
    max_press_a = 100
    max_press_b = 100
    m_costs = []
    for machine in configs:
        ba, bb, prize = machine
        px, py = prize
        bax, bay = ba
        bbx, bby = bb
        cost = -1

        press_a = 0
        while press_a <= max_press_a or press_a * bax <= px:
            rem = px - (press_a * bax)
            press_b = rem // bbx if rem % bbx == 0 else None
            if press_b is not None and press_b <= max_press_b:
                if press_a * bay + press_b * bby == py:
                    cost = cost_a * press_a + cost_b * press_b
                    break

            press_a += 1

        m_costs.append(cost)

    total_cost = sum(c for c in m_costs if c != -1)
    return total_cost


def calc_press_b(px, py, bax, bay, bby, bbx):
    num = px * bay - py * bax
    denom = bbx * bay - bby * bax
    return num / denom


def calc_press_a(px, py, bax, bay, bby, bbx):
    num = px * bby - py * bbx
    denom = bby * bax - bbx * bay
    return num / denom


def p2(configs):
    cost_a = 3
    cost_b = 1
    m_costs = []
    for machine in configs:
        ba, bb, prize = machine
        px, py = prize
        px, py = px + 10000000000000, py + 10000000000000
        bax, bay = ba
        bbx, bby = bb
        cost = -1
        press_b = max(calc_press_b(px, py, bax, bay, bby, bbx), 0)
        press_a = max(calc_press_a(px, py, bax, bay, bby, bbx), 0)
        if int(press_a) * bax + int(press_b) * bbx == px:
            cost = press_a * cost_a + press_b * cost_b
        m_costs.append(int(cost))

    total_cost = sum(c for c in m_costs if c != -1)
    return total_cost


if __name__ == "__main__":
    print(p1(load("./2024/d13-sample.txt")))
    print(p1(load("./2024/d13-sample-2.txt")))
    print(p1(load("./2024/d13.txt")))

    # Part 2
    print(p2(load("./2024/d13-sample.txt")))
    print(p2(load("./2024/d13-sample-2.txt")))
    print(p2(load("./2024/d13.txt")))
