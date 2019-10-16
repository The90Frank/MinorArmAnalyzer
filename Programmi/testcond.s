	.section .text
	.global _start

_start:
	mov r0, #42
	mov r1, #42
	
	subs r2, r0, r1
	nop
	
	nop
	movpl r0, #33
	
	mov r7, #1
	SVC 0
