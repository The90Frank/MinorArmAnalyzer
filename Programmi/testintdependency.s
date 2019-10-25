	.section .text
	.global _start

_start:
	mov r0, #21
	add r0, r0, r0
	mov r7, #1
	SVC 0
