library IEEE;
use IEEE.STD_LOGIC_1164.ALL;


entity MuxNextRD is
    Port ( RD : in  STD_LOGIC_VECTOR(5 downto 0);
           O7 : in  STD_LOGIC_VECTOR(5 downto 0);
			  RfDest: in STD_LOGIC;
           NRd : out  STD_LOGIC_VECTOR(5 downto 0)
			  );
end MuxNextRD;

architecture Behavioral of MuxNextRD is

begin

	process(RD,RfDest)
		begin
			if (RfDest='0') then
				NRd<=RD;
			else 
				NRd<=O7;
			end if;
	end process;
end Behavioral;

