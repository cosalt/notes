        INP
        STA 99
        LDA ONE
        STA 28
LOOP    LDA 99
        SUB 28
        STA 99
        OUT
        BRZ FINISH
        BRP LOOP
FINISH  LDA 98
ONE     DAT 1
