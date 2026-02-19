	.section .text
	.global _start

_start:
	mov r0, #42
	nop
	mov r7, #1
	SVC 0
