# tc-calc（小工具）

用于把“每个温度点的两态峰数据”快速换算成可直接粘贴到 Excel / Origin 的结果（TSV）。

---

## 工作流（与你的日常一致）
1) TopSpin：对同一温度点的两态峰（t 峰 / c 峰）做积分或读取峰参数
2) 本工具：输入 5 个数 → 输出一行 TSV
3) Excel：把多行 TSV 贴成一张表（每个温度点一行）
4) Origin：作图/拟合  
   - 线性拟合：用 `Lnk` 与 `invT(=1/T)`  
   - 非线性作图/拟合：用 `Gt-c` 与 `T_K`（拟合公式由使用者在 Origin 内自定义）

---

## 1）输入顺序（必须按这个顺序）
一行 5 个数，用空格/逗号/Tab 分隔：

`T_K  t_raw1  t_raw2  c_raw1  c_raw2`

说明：
- `T_K`：温度（K）
- `t_raw1*t_raw2`：t 峰的“面积/强度代理”
- `c_raw1*c_raw2`：c 峰的“面积/强度代理”
- `t_raw1/t_raw2/c_raw1/c_raw2` 来自 TopSpin 峰表中你选择的两列（常见做法如 `Height × Linewidth`）。
- 如果你在 TopSpin 里**直接有积分面积/Volume/Integral**：可以填 `raw1=面积`，`raw2=1`（这样乘积仍等于面积）。

示例：
`278  32210.8  98.976  39777.79  92.251`

---

## 2）输出列（TSV，可直接复制）
输出一行（含表头），列顺序：

`t  c  invT  Lnk  Lnk'  T_K  Gt-c  Gc-t`

用于 Origin：
- 线性拟合：`invT`（X） vs `Lnk`（Y）
- 非线性作图：`T_K`（X） vs `Gt-c`（Y）

---

## 3）计算公式（工具口径）
- `t = t_raw1 * t_raw2`
- `c = c_raw1 * c_raw2`
- `k = t / c`
- `Lnk = ln(k)`
- `invT = 1 / T_K`
- `Gt-c = -(1.987 * T_K * Lnk) / 1000`
- `Gc-t = -Gt-c`

---

## 使用方式
- `tc_calc.html`：浏览器打开（手机/电脑都可）
- `tc_calc.py`：命令行运行
