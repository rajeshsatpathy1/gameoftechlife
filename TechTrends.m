M = 20;
N = 20;
p = 0.03;
f = p *0.0001;

p1 = 0.02;
f1 = p * 0.0001;
x = 500
F = (rand(M, N) < p)+1; %countries with probability p
F1 = F + (rand(M, N) < p1)+2;

colormap([0.5,0.5,.5;0,1,0;0,0,1;1,0,0]);
montage(image(F),image(F1));