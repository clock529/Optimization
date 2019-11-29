function [result] = fun(x, r)
result = (x(1) - 20) ^2 + (x(2) - 15) ^ 2 + r * (1/x(1) + 1/x(2) + 1/(20 - (x(1) + x(2))));