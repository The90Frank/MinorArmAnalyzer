	.section .text
	.global _start

_start:
	mov r1, #7
	mov r2, #6
	mul r0, r1, r2
	nop
	mov r7, #1
	SVC 0
