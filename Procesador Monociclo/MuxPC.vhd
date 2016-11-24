library IEEE;
use IEEE.STD_LOGIC_1164.ALL;


entity MuxPC is
    Port ( PCdisp30 : in  STD_LOGIC_VECTOR(31 downto 0);
           PCdisp22 : in  STD_LOGIC_VECTOR(31 downto 0);
           PC : in  STD_LOGIC_VECTOR(31 downto 0);
			  PCplus1 : in  STD_LOGIC_VECTOR(31 downto 0);
			  PCSource: in STD_LOGIC_VECTOR(1 downto 0);
           nPC : out  STD_LOGIC_VECTOR(31 downto 0)
			  );
end MuxPC;

architecture Behavioral of MuxPC is

begin
	process(PCdisp30,PCdisp22,PC,PCSource)
	begin
		if (PCSource="10") then
			nPC <= PCdisp22;
		elsif (PCsource="01") then
			nPC <= PCdisp30;
		elsif (PCSource="00") then
			nPC <= PC;
		else
			nPC <= PCplus1;
		end if;
	end process;
end Behavioral;

