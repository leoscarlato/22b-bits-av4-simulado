leaw $SP, %A
movw (%A), %A
subw %A, $1, %D
leaw $SP, %A
movw %D, (%A)
movw %D, %A
movw (%A), %D
leaw $5, %A
movw %D, (%A)
leaw $SP, %A
movw (%A), %A
decw %A
movw (%A), %D
incw %A
movw %D, (%A)
leaw $5, %A
movw (%A), %D
leaw $SP, %A
movw (%A), %A
decw %A
movw %D, (%A)
leaw $258, %A
movw %A, %D
leaw $0, %A
movw %D, (%A)
