	.section .text
	.global _start

_start:
    mov r4, #42
    mov r5, #4
    mov r6, #33
    nop

    stm sp,{r0-r10}
    ldm sp,{r0-r11}

    mov r7, #1
	mov r9, #5
    mov r9, #10
    SVC 0
