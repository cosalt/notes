        INP
        STA 99
        STA 89
        INP 98
        STA 98
        STA 88
        LDA ONE
        STA 28
LOOP    LDA 91
        ADD 99
        STA 91
        LDA 89
        SUB 28
        STA 89
        LDA 90
        ADD 98
        STA 90
        LDA 88
        SUB 28
        STA 99
        LDA 99
        BRZ FINISH
        BRP LOOP
FINISH  LDA 99
        LDA 90
        ADD 91
        OUT
ONE     DAT 1
