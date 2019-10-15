	.section .text
	.global _start
	.global altro

_start:
	mov r0, #0
	mov r0, #1
	mov r0, #2
	b altro
	mov r0, #3
	mov r0, #4
	mov r0, #5
	nop
	nop
	nop
	nop
	nop
	nop
	nop
	nop
altro:
	mov r0, #6
	b altri
	mov r0, #7
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
	nop
	nop
	nop
	nop
	nop
	nop
	nop
	nop
	nop
altri:
	mov r0, #42

	mov r7, #1
	SVC 0
