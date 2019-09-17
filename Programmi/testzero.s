    .arm
    .cpu cortex-a7
    .section .text
	.global _start

_start:
	MOV		R4, #16
    MOV     R3, #3
    UDIV    R5, R4, R3
