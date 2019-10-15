    .cpu cortex-a7
    .section .text
	.global _start

_start:
    ldr r4, [r13,r4]
    ldr r5, [r13,r5]
    udiv r8, r4, r5

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
