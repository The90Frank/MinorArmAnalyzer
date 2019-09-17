	.section .text
	.global _start

_start:
	MOV		R2, #0x10000
	MOV		R1, #16
	NOP @MOV		R8, #42
	NOP @STR		R8, [R2, R1]
	NOP
	NOP
	NOP
	NOP
	NOP
	LDR		R9, [R13, R1]   
