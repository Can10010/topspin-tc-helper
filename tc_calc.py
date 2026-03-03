import math

R_CAL = 1.987
DIV_1000 = 1000

PROMPT = (
    "请依次输入 5 个数，并用空格分隔：\n"
    "T_K  t_raw1  t_raw2  c_raw1  c_raw2\n"
    "示例：278  32210.8  98.976  39777.79  92.251\n"
    "输入> "
)

def parse_five(line: str):
    parts = [p for p in line.replace(",", " ").split() if p.strip()]
    if len(parts) != 5:
        raise ValueError(f"需要 5 个数，但你输入了 {len(parts)} 个。")
    return [float(x) for x in parts]

def main():
    print("=== t/c 极简计算器 ===")
    print("（每次输入一行 5 个数；Ctrl+C 退出）\n")

    while True:
        try:
            line = input(PROMPT).strip()
            if not line:
                print("⚠️ 你输入了空行，请重新输入。\n")
                continue

            T_K, t_raw1, t_raw2, c_raw1, c_raw2 = parse_five(line)

            t = t_raw1 * t_raw2
            c = c_raw1 * c_raw2
            invT = 1.0 / T_K
            k = t / c
            lnk = math.log(k)
            lnk_p = -lnk
            G_t_c = -(R_CAL * T_K * lnk) / DIV_1000
            G_c_t = -G_t_c

            print("\nTSV(可直接复制)：")
            print("t\tc\tinvT\tLnk\tLnk'\tT_K\tGt-c\tGc-t")
            print(f"{t}\t{c}\t{invT}\t{lnk}\t{lnk_p}\t{T_K}\t{G_t_c}\t{G_c_t}")
            print("提示：线性拟合请用 invT(=1/T) 与 Lnk（或 Lnk'），非线性拟合/作图用 T_K 与 Gt-c。")
            print("\n----------------------\n")

        except Exception as e:
            print(f"⚠️ 无法计算：{e}")
            print("请按顺序输入：T_K t_raw1 t_raw2 c_raw1 c_raw2（空格分隔）\n")

if __name__ == "__main__":
    main()