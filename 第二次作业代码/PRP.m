function result = PRP(x, r)

k = 1;
g = gfun(x, r);
p = -g;
while g'*g > 1e-6
   alpha = minf(x, p, r);
   x = x + alpha * p;
   new_g = gfun(x, r);
   beta = new_g'*(new_g - g)/(g'*g);
   p = -new_g + beta * p;
   g = new_g;
   k = k + 1;
   if k == 3
       p = -g;
   end
end
result = x;