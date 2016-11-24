library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux32b is
	PORT( A  : in  STD_LOGIC_VECTOR (31 downto 0);
		   B  : in  STD_LOGIC_VECTOR (31 downto 0);
			Sel: in  STD_LOGIC;
			O  : out STD_LOGIC_VECTOR (31 downto 0));
end mux32b;

architecture arqMux32b of mux32b is

begin

	process(A, B, Sel)
	begin
		if (Sel = '1') then
			O <= B;
		else
			if(Sel = '0') then
				O <= A;
			end if;
		end if;
	end process;

end arqMux32b;

