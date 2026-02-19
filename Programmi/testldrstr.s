	.section .text
	.global _start
	.global pippo
    .global pluto

_start:
    mov r4, #42
    mov r5, #4
    mov r6, #33
    nop
    stm sp,{r0-r10}
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

pippo:
    ldr r0,[sp,#0]
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

pluto:
    str r0,[sp,#0]
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
    
    mov r7, #1
    SVC 0
