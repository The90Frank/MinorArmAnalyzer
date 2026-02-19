	.section .text
	.global _start
	.global lab
_start:
		movs		r0, #1
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop

lab:
        nop
        nop
        bne		lab
        nop
        subs	r0,r0,#2
		nop
        nop
        nop
        nop
        nop
		bne		lab
        nop
