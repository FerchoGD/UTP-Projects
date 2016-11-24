library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity sign_ext_unit is
	Port( entrada  : in  STD_LOGIC_VECTOR (12 downto 0);
			salida : out STD_LOGIC_VECTOR (31 downto 0)
	);
end sign_ext_unit;

architecture ArqSignExt of sign_ext_unit is


begin
	
	process(entrada)
	begin
		if (entrada(12) = '1') then
			salida <= "1111111111111111111" & entrada;
		else
			salida <= "0000000000000000000" & entrada;
		end if;
	end process;

end ArqSignExt;

