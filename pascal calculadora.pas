program Calculadora;
{$mode objfpc}{$H+}
uses Math, SysUtils;

type
  TCalculadora = object
    function Sumar(a, b: Integer): Integer;
    function Restar(a, b: Integer): Integer;
    function Multiplicar(a, b: Integer): Integer;
    function Dividir(a, b: Integer): Real;
    function RaizCuadrada(a: Integer): Real;
  end;

function TCalculadora.Sumar(a, b: Integer): Integer;
begin
  Result := a + b;
end;

function TCalculadora.Restar(a, b: Integer): Integer;
begin
  Result := a - b;
end;

function TCalculadora.Multiplicar(a, b: Integer): Integer;
begin
  Result := a * b;
end;

function TCalculadora.Dividir(a, b: Integer): Real;
begin
  if b <> 0 then
    Result := a / b
  else
    Result := 0; // Evita la división por cero.
end;

function TCalculadora.RaizCuadrada(a: Integer): Real;
begin
  Result := Sqrt(a);
end;

var
  Calc: TCalculadora;
  a, b: Integer;
begin
  Write('Introduce el primer número: ');
  ReadLn(a);
  Write('Introduce el segundo número: ');
  ReadLn(b);

  WriteLn('La suma de ', a, ' y ', b, ' es ', Calc.Sumar(a, b));
  WriteLn('La resta de ', a, ' y ', b, ' es ', Calc.Restar(a, b));
  WriteLn('La multiplicación de ', a, ' y ', b, ' es ', Calc.Multiplicar(a, b));

  if (b <> 0) then 
    WriteLn('La división de ', a, ' entre ', b, ' es ', Format('%0.2f', [Calc.Dividir(a, b)]))
  else 
    WriteLn('No se puede dividir por cero.');

  WriteLn('La raíz cuadrada de ', a, ' es ', Format('%0.2f', [Calc.RaizCuadrada(a)]));
end.
