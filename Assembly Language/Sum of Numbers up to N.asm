        INP
        STA 99
        LDA ONE
        STA 28
        LDA 99
        STA 98
LOOP    LDA 99
        SUB 28
        STA 99
        LDA 98
        ADD 99
        STA 98
        LDA 99
        BRZ FINISH
        BRP LOOP
FINISH  LDA 98
        OUT
ONE     DAT 1
