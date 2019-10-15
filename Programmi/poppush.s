	.section .text
	.global _start

_start:
    mov r4, #42
    mov r5, #4
    mov r6, #33
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    
    push {R0,R4-R6}
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
