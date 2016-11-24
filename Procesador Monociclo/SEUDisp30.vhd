library IEEE;
use IEEE.STD_LOGIC_1164.ALL;


entity SEUDisp30 is
    Port ( Disp30 : in  STD_LOGIC_VECTOR(29 downto 0);
           S : out  STD_LOGIC_VECTOR(31 downto 0)
			  );
end SEUDisp30;

architecture Behavioral of SEUDisp30 is

begin
	process(Disp30)
	begin
		S(31) <= Disp30(29);
		S(30) <= Disp30(29);
		S(29 downto 0) <= Disp30;
	end process;
end Behavioral;

