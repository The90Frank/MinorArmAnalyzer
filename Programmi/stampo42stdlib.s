.cpu cortex-a65ae
.data
    rdf: .asciz "La risposta alla domanda fondamentale sulla vita,l’universo e tutto quanto è: %d\n"
.text
    .global main
main:
    mov x1, #21
    mov x2, #2
    mul x1, x1, x2
    bl write
    mov x8, #93
    svc 0
write:
    stp x29, x30, [sp, #-16]!
    ldr x0, =rdf
    bl printf
    ldp x29, x30, [sp], #16
    ret
