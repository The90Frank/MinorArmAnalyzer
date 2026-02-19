	.section .text
	.global _start

_start:
	mov x1, #42
	LDURSH x1, [sp, #42]
	mov x0, x1
	nop
	mov x8, #93
	SVC 0
