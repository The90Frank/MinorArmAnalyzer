.data
    val_integ: .asciz "Il valore di integral : %d\n"
.text
.global main
main:
    mov x2, #0 //valore di a
    mov x3, #7 //valore di b
    mov x4, #2 //valore di d
    //utilizzo x1 come indice
    mov x1, x2 //x=a
    mov x9, #0 //integral
for:
    //si suppone che almeno un ciclo venga effettuato
    bl funa
    add x9, x9, x10 //integral + f(x)
    mul x9, x9, x4 //(integral + f(x))*d
    add x1, x1, x4 //x+=d
    cmp x1, x3
    bmi for
    //stampo valore
    bl write
    mov x8, #93
    svc 0
funa:
    stp x29, x30, [sp, #-16]!
    mov x5, #3
    mul x10, x1, x1
    mul x11, x1, x5
    add x10, x10, x11
    sub x10, x10, #4
    ldp x29, x30, [sp], #16
    ret
write:
    stp x29, x30, [sp, #-16]!
    //stampo il valore di integral
    ldr x0, =val_integ
    mov x1, x9
    bl printf
    ldp x29, x30, [sp], #16
    ret
