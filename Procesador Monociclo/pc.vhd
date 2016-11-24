library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity pc is
	PORT( clk : in STD_LOGIC;
			rst : in STD_LOGIC;
			address : in STD_LOGIC_VECTOR (31 downto 0);
			sig : out STD_LOGIC_VECTOR (31 downto 0)
	);
end pc;

architecture ArqPC of pc is

begin
	process(clk, address, rst)
	begin
		if (rst = '1')then
		    sig <= (others => '0');
		else
			if(rising_edge(clk))then
				sig <= address;
			end if;
		end if;
	end process;
		


end ArqPC;

