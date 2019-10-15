	.section .text
	.global _start

_start:
    mov r4, #42
    mov r5, #4
    str r4, [r13,r5]
    nop
    nop
    nop
    nop
    nop
    nop
    nop

    ldr r6, [r13,r5]
    add r8, r6, r4
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
    nop
    nop
    nop
    nop

    nop
	mov	r0, #0
	mov r7, #1
	SVC 0
