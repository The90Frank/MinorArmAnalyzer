	.section .text
	.global _start

_start:
	MOV		R0, #0x10000
	MOV		R1, #0x10000
	ADD		R1, #0x100
	MOV		R2, #0
	MOV		R3, #52
		
WHILE:
	CMP		R2, R3
	BPL		DONE
	ADD		R8, R2, #10
	ADD		R9, R2, #7
	STR		R8, [R0, R2]
	STR		R9, [R1, R2]
	ADD		R2, R2, #4
	B		WHILE

DONE:
	MOV		R2, #0
	MOV		R3, #52
	MOV		R5, #0x1300
		
LOOP:		
	CMP		R2, R3
	BPL		DONE2
	LDR		R8, [R1, R2]
	LDR		R9, [R0, R2]
	ADD		R12, R12, R9
	SUB		R8, R8, R9
	CMP		R8, R4
	BPL		CONT
	SUB		R3, R3, #4
	STR		R8, [R5, R3]
	B		LOOP
	
CONT:		
	ADD		R2, R2, #4
	B		LOOP

DONE2:

