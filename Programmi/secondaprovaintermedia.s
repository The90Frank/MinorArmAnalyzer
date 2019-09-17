		MOV		R0, #0x1100 ;base address di A
		MOV		R1, #0x1200 ;base address di B
		MOV		R2, #0 ;indice
		MOV		R3, #52 ;array dim di A e B
		
WHILE
		CMP		R2, R3
		BPL		DONE
		ADD		R8, R2, #10
		ADD		R9, R2, #7
		STR		R8, [R0, R2]
		STR		R9, [R1, R2]
		ADD		R2, R2, #4
		B		WHILE
DONE
		MOV		R2, #0 ;indice i=0
		MOV		R3, #52 ;indice j=N
		MOV		R5, #0x1300 ;base address di C
		
LOOP		CMP		R2, R3
		BPL		DONE2 ; if i > j
		LDR		R8, [R1, R2] ;A
		LDR		R9, [R0, R2] ;B
		ADD		R12, R12, R9 ;temp=B[i]+temp
		SUB		R8, R8, R9 ;A[i]-B[i]
		CMP		R8, R4 ;uso R4 come mio zero è per verificare che R8 > 0
		BPL		CONT
		SUB		R3, R3, #4 ;j--
		STR		R8, [R5, R3] ; C[j]=R8
		B		LOOP
		
CONT		ADD		R2, R2, #4 ;i++
		B		LOOP
		
DONE2	END
		
