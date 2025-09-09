# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_full_adder(dut):
    """Test Full Adder functionality"""

    dut._log.info("Starting Full Adder Test")

    # Define test cases as tuples: (a, b, cin, expected_sum, expected_cout)
    test_vectors = [
        (0, 0, 0, 0, 0),
        (0, 0, 1, 1, 0),
        (0, 1, 0, 1, 0),
        (0, 1, 1, 0, 1),
        (1, 0, 0, 1, 0),
        (1, 0, 1, 0, 1),
        (1, 1, 0, 0, 1),
        (1, 1, 1, 1, 1),
    ]

    for a, b, cin, expected_sum, expected_cout in test_vectors:
        dut.a.value = a
        dut.b.value = b
        dut.cin.value = cin

        await Timer(1, units="ns")  # Small delay for propagation

        assert dut.sum.value == expected_sum, f"Sum mismatch: {a}+{b}+{cin} expected {expected_sum}, got {int(dut.sum.value)}"
        assert dut.cout.value == expected_cout, f"Cout mismatch: {a}+{b}+{cin} expected {expected_cout}, got {int(dut.cout.value)}"

        dut._log.info(f"Test Passed for a={a}, b={b}, cin={cin}")
