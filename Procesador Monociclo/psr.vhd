----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    16:25:06 10/20/2016 
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;


entity psr is
Port(
	clk   : in std_logic;
	reset : in std_logic;
	nzvc  : in  std_logic_vector(3 downto 0);
	ncwp : in std_logic;
	carry : out std_logic;
	cwp : out std_logic
);
end psr;
architecture psrArq of psr is


signal PSRDATA : std_logic_vector (3 downto 0) := "0000";

begin

process(clk,nzvc,ncwp,reset)
begin

	if (reset='1') then
		PSRDATA<= "0000";
		carry<= '0';
		cwp <= '0';
	else	
		if (rising_edge(clk))then
			PSRDATA<= nzvc;
			carry<=PSRDATA(0);
			cwp <= ncwp;
		end if;
	end if;
end process;

end psrArq;

