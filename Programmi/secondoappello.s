		;fase	di caricamento valori in A e in B
		MOV		R0, #0x1100 ;base address di A
		MOV		R1, #0x1200 ;base address di B
		MOV		R2, #0 ;indice
		MOV		R3, #50 ;N
		
WHILE
		CMP		R2, R3
		BPL		DONE
		ADD		R8, R2, #10 ;ogni valore di A è dato dalla somma di i e 10
		ADD		R9, R2, #7 ;ogni valore di B è dato dalla somma di i e 7
		STR		R8, [R0, R2] ;memorizzo il valore di A
		STR		R9, [R1, R2] ;memorizzo il valore di B
		ADD		R2, R2, #8 ;incremento i
		B		WHILE
DONE
		MOV		R2, #0
		MOV		R4, #42 ;MAX
		;R10		è x e R12 è temp
WHILE2	CMP		R10, R4
		BPL		DONE2
		LDR		R8,[R0, R2]
		LDR		R9,[R1, R2]
		ADD		R12, R8, R9
		CMP		R5, R12
		BPL		NEG
JU		ADD		R10, R10, R12
		ADD		R2, R2, #8
		CMP		R2, R3
		BEQ		BREAK
		B		WHILE2
		
NEG		SUB		R12, R11, R12 ;R11 è sempre uguale a zero, mi serve per temp=-temp
		B		JU
		
BREAK	END
		
DONE2	END
		
