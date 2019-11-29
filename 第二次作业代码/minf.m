function [alpha] =  minf(x, p, r)
a = 0;
b = 1;
eps = 1e-3;
x1 = a+0.382*(b-a);
x2 = a +0.618*(b-a);
f1 = fun(x + x1 * p, r);
f2 = fun(x + x2 * p, r);
while abs(b-a)>eps
    if f1>f2
        a = x1;
        x1 = x2;
        x2 = a +0.618*(b-a);
        f1 = f2;
        f2 = fun(x + x2 * p, r);
    else
        b = x2;
        x2 = x1;
        x1 = a+0.382*(b-a);
        f2 = f1;
        f1 = fun(x + x1 * p, r);
    end
end
alpha =(b+a)/2;