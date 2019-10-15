	.section .text
	.global _start

_start:
	mov r1, #672
	mov r2, #16
	udiv r0, r1, r2
	nop
	mov r7, #1
	SVC 0
