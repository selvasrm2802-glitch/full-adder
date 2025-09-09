`default_nettype none
`timescale 1ns / 1ps

module tt_um_example (
    input  wire [7:0] ui_in,    // Inputs (use [0]=a, [1]=b, [2]=cin)
    output wire [7:0] uo_out,   // Outputs (use [0]=sum, [1]=cout)
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    // Drive unused signals
    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

    // Extract inputs
    wire a   = ui_in[0];
    wire b   = ui_in[1];
    wire cin = ui_in[2];

    // Outputs
    reg sum;
    reg cout;

    always @(*) begin
        if (!rst_n) begin
            sum  = 1'b0;
            cout = 1'b0;
        end else begin
            sum  = a ^ b ^ cin;
            cout = (a & b) | (b & cin) | (a & cin);
        end
    end

    assign uo_out[0] = sum;
    assign uo_out[1] = cout;
    assign uo_out[7:2] = 6'b0; // Unused outputs

endmodule
