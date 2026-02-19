	.section .text
	.global _start
    .global _full

_start:
	mov r4, #42
	mov r5, #21
    mov r6, #128
    mov r7, #16
    mov r8, #0
	mov r9, #8
    mov r10, #87
    mov r11, #3
    nop
    nop
_full:
    udiv r3, r10, r5
    add r1,r4,r6
    sub r2, r8, r10
    mul r0, r7, r5
    str r4, [sp, r9]
    lsl r6, r9, r9
    ldr r0, [r0, r0]
    add r3, pc, r8
    mul r8, r11, r6
    b _full

	mov r7, #1
	SVC 0
