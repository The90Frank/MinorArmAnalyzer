	.section .text
	.global _start

_start:
	mov r1, #42
	mov r2, #16
	str r1, [sp, r1]
	ldr r2, [sp, r2]
	nop
	mov r0, r2
	mov r7, #1
	SVC 0
