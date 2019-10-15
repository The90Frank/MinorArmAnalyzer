	.section .text
	.global _start

_start:
    mov r4, #42
    mov r5, #4
    mov r6, #33
    nop

    stm sp,{r4,r5,r6}
    ldm sp,{r0-r2}

	mov r7, #1
	SVC 0
