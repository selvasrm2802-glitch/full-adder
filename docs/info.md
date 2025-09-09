<!---
This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

# Full Adder

## How it works

A Full Adder is a basic combinational digital circuit that adds three binary inputs and produces two outputs:

**Inputs:**
- `A` → First binary input
- `B` → Second binary input
- `Cin` → Carry-in (from previous stage in multi-bit addition)

**Outputs:**
- `Sum` → Sum of the inputs
- `Cout` → Carry-out (to the next stage)

**Logic Equations:**
- `Sum = A ⊕ B ⊕ Cin`
- `Cout = (A & B) | (B & Cin) | (A & Cin)`

---

## How to test
Pin mapping:

Inputs:

A = ui_in[0]

B = ui_in[1]

Cin = ui_in[2]

Outputs:

Sum = uo_out[0]

Cout = uo_out[1]

Apply the following truth table values and check outputs:

A	B	Cin	Sum	Cout
0	0	0	0	0
0	0	1	1	0
0	1	0	1	0
0	1	1	0	1
1	0	0	1	0
1	0	1	0	1
1	1	0	0	1
1	1	1	1	1

External hardware
None
