	.section .text
	.global _start

_start:
	mov r1, #42
	ldr r2, [sp, #0]
	udiv r0, r1, r2
	nop
	mov r7, #1
	SVC 0
