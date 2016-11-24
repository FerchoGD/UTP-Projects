library IEEE;
use IEEE.STD_LOGIC_1164.ALL;


entity MuxDWR is
    Port ( DM : in  STD_LOGIC_VECTOR(31 downto 0);
           AluR : in  STD_LOGIC_VECTOR(31 downto 0);
			  PC: in STD_LOGIC_VECTOR(31 downto 0);
			  RFSource: in STD_LOGIC_VECTOR(1 downto 0);
           DTRF : out  STD_LOGIC_VECTOR(31 downto 0)
			  );
end MuxDWR;

architecture Behavioral of MuxDWR is

begin
	process(DM,AluR,RFSource)
		begin
			if(RFSource="00") then
				DTRF<=AluR;
			elsif (RFSource="01") then
				DTRF<=DM;
			elsif (RFsource="10") then
				DTRF<=PC;
			else
				DTRF<=AluR;
			end if;
	end process;

end Behavioral;

