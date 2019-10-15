	.section .text
	.global _start

_start:
    mov r0, #0
    mov r1, #4
    nop 
    nop
    nop
    nop
    nop
    nop 
    nop
    nop
    nop
    nop

    mov r4, r15
    mov r5, r15
    str r15, [sp, r0]
    str r15, [sp, r1]
    ldr r8, [sp, r0]
    ldr r9, [sp, r1]

    nop 
    nop
    nop
    nop
    nop
    nop 
    nop
    nop
    nop
    nop

	mov r7, #1
	SVC 0
