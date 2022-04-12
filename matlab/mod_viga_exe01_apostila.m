% -------------------------------------------------
%       Codigo Matlab para implementacao
%           de modelo de viga
% -------------------------------------------------
%       Modelo de Viga: Exemplo 01 da apostila
% -------------------------------------------------
clc, clear, close all
l=2; % comprimento da viga [m]
q0=100; % carregamento distribuido [N/m]

% dimensoes da secao
h = 100/1000; 
b = 100/1000;
Izz=(b*h^3)/12;
% propriedades do material
E=200E9; % Aco

% dominio estrutural
dx=0.001;
dy=0.001;
x=0:dx:l;
y=-h:dy:h;
Vy = zeros(1,size(x,2)); 
Mz = zeros(1,size(x,2)); 
The = zeros(1,size(x,2)); 
v = zeros(1,size(x,2)); 
% loop de integracao 
for i=1:size(x,2)
    if x(i)<l/2
        Vy(i) = -q0*(x(i)^1)+3*q0*l/8;
        Mz(i) = -(q0/2)*(x(i)^2)+3*q0*l*x(i)/8;
        The(i) = -(q0/6)*(x(i)^3)+(3*q0*l*x(i)^2)/16 - (3*q0*l^3)/128;
        v(i) = -(q0/24)*(x(i)^4)+(q0*l*x(i)^3)/16 - (3*q0*l^3*x(i))/128;
    else
        Vy(i) = -q0*(x(i)^1-(x(i)-l/2)^1)+3*q0*l/8;
        Mz(i) = -(q0/2)*(x(i)^2-(x(i)-l/2)^2)+3*q0*l*x(i)/8;
        The(i) = -(q0/6)*(x(i)^3-(x(i)-l/2)^3)+(3*q0*l*x(i)^2)/16 - (3*q0*l^3)/128;
        v(i) = -(q0/24)*(x(i)^4-(x(i)-l/2)^4)+(q0*l*x(i)^3)/16 - (3*q0*l^3*x(i))/128;
    end
end
figure()
subplot(4,1,1)
plot(1000.*x,Vy)
ylabel('Vy(x) [N]')
title('Esforco Cortante')
grid on
subplot(4,1,2)
plot(1000.*x,Mz)
ylabel('Mz(x) [N.m]')
title('Momento Fletor')
grid on
subplot(4,1,3)
plot(1000.*x,The./(E*Izz))
ylabel('The(x) [rad]')
title('Inclinacaoo da curvatura da viga')
grid on
subplot(4,1,4)
plot(1000.*x,1000*v./(E*Izz))
xlabel('L [mm]')
ylabel('v(x) [mm]')
title('Deslocamento da curvatura da viga')
grid on

figure()
[X,Y]=meshgrid(x,y);
Mz_xy = Mz.*(ones(size(y,2),size(x,2)));
Sigxx=-((Y./Izz).*Mz_xy);
contour(X,Y,Sigxx./1E6,8,'ShowText','on')
title('Tensao Normal [MPa]')
xlabel('L')
ylabel('h')
grid on