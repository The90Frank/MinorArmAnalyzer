	.section .text
	.global _start

_start:
	MOV		R1, #16
	NOP @MOV		R8, #42
	NOP @STR		R8, [R2, R1]
	NOP
	NOP
	NOP
	NOP
	NOP
	MOV		R0, #42
	STR		R0, [R13, R1]   
