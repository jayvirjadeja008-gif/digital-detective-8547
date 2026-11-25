# Task 5.1 — Convert numbers by hand

| Question | Working and answer |
|---|---|
| Convert decimal 13 to binary | Divide repeatedly by 2: 13 = 8 + 4 + 1, so the binary digits are `1101₂`. |
| Convert decimal 25 to binary | Divide repeatedly by 2: 25 = 16 + 8 + 1, so `11001₂`. |
| Convert binary 1010 to decimal | 1×8 + 0×4 + 1×2 + 0×1 = `10₁₀`. |
| Convert binary 1101 to decimal | 1×8 + 1×4 + 0×2 + 1×1 = `13₁₀`. |
| Convert hexadecimal A to decimal | A = 10, so `10₁₀`. |
| Convert hexadecimal 1F to decimal | 1×16 + 15×1 = `31₁₀`. |
| Convert binary 1111 to hexadecimal | 1111₂ = 15₁₀ = `F₁₆`. |

# Task 5.2 — Verify using Python

| Expression tested | Python result | Manual match? |
|---|---|---|
| `bin(13)` | `0b1101` | Yes |
| `bin(25)` | `0b11001` | Yes |
| `int("1010", 2)` | `10` | Yes |
| `int("1101", 2)` | `13` | Yes |
| `hex(10)` | `0xa` | Yes |
| `int("1F", 16)` | `31` | Yes |
| `hex(int("1111", 2))` | `0xf` | Yes |
