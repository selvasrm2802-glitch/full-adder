import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_full_adder(dut):
    """Test Full Adder functionality using TinyTapeout interface"""

    dut._log.info("Starting Full Adder Test")

    # Initialize control signals
    dut.clk.value = 0
    dut.rst_n.value = 1
    dut.ena.value = 1
    dut.uio_in.value = 0

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
        # Encode inputs into ui_in[0:2]
        dut.ui_in.value = (a << 0) | (b << 1) | (cin << 2)

        await Timer(1, units="ns")

        # Extract outputs from uo_out[0:1]
        sum_val = (dut.uo_out.value >> 0) & 1
        cout_val = (dut.uo_out.value >> 1) & 1

        assert sum_val == expected_sum, f"Sum mismatch: a={a}, b={b}, cin={cin}, expected {expected_sum}, got {sum_val}"
        assert cout_val == expected_cout, f"Cout mismatch: a={a}, b={b}, cin={cin}, expected {expected_cout}, got {cout_val}"

        dut._log.info(f"PASS: a={a}, b={b}, cin={cin} -> sum={sum_val}, cout={cout_val}")
