# Test Cases — Employee Salary Calculator

Assumptions: HRA = 20% of basic, DA = 10%, PF deduction = 12%. Gross = basic + HRA + DA; net = gross − PF.

| # | Name | Basic salary (Rs.) | Expected result |
|---|---|---:|---|
| 1 | Ravi | 10000 | HRA 2000, DA 1000, PF 1200, gross 13000, net 11800 |
| 2 | Asha | 0 | All salary components are Rs. 0.0 |
| 3 | Kiran | 25000 | HRA 5000, DA 2500, PF 3000, gross 32500, net 29500 |
| 4 | Mina | 15000.50 | HRA 3000.1, DA 1500.05, PF 1800.06, gross 19500.65, net 17700.59 (rounded for display) |
| 5 | Sam | -100 | Invalid salary |

Note: percentages are classroom assumptions and should be changed if the faculty provides different rules.