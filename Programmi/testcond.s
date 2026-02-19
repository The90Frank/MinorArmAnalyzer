	.section .text
	.global _start

_start:
	subs	r2, r1, r0
	nop
	
	nop
	movpl r0, #33
	
	mov r7, #1
	SVC 0
