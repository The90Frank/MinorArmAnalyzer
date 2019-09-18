	.section .text
	.global _start

_start:
	mov	r5, #84
	mov	r6, #42
	nop
	nop
	mov r7, #1
	SVC 0
