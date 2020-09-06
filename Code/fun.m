function y = fun(x)
A = 1;
B = 0.02;
C1 = 0.8;
C2 = -5.6;
y = A * exp( -B * (x+C2) ) + C1;
end
