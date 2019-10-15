	.section .text
	.global _start
    .global fine

_start:
    mov r4, #0xe3a0
    lsl r4, #8
    add r4, r4, #0x00
    lsl r4, #8
    add r4, r4, #0x2a

    mov r6, #0xe1a0
    lsl r6, #8
    add r6, r6, #0xf0
    lsl r6, #8
    add r6, r6, #0x0e

    add lr, pc, #4
    push {r4, r6}
    mov pc, sp
    
    nop
    nop
    nop
    nop
    nop 
    nop
fine:
	mov r7, #1
	SVC 0
