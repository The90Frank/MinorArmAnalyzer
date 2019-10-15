	.section .text
	.global _start
	.global teststarting

_start:
	mov	x0, #10
	mov	x1, #11
	mov	x2, #12
	mov	x3, #13
	mov	x4, #14
	mov	x5, #15
	mov	x6, #16
	mov	x7, #17
	mov	x8, #18
	mov	x9, #19
	mov	x10, #20
	mov	x11, #21
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
teststarting:
	udiv x12, x7, x6
	mul x1, x5, x4
	
	nop
	nop
	nop
	nop
	nop
	nop




	mov x7, #1
	SVC 0
