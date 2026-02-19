	.section .text
	.global _start

_start:
    mov r0, #0
    nop
    mov r4, r15
    mov r5, r15
    nop
    nop

	mov r7, #1
	SVC 0
