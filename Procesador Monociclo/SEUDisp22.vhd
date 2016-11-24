library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity SEUDisp22 is
    Port ( Disp22 : in  STD_LOGIC_VECTOR(21 downto 0);
           S : out  STD_LOGIC_VECTOR(31 downto 0)
			  );
end SEUDisp22;

architecture Behavioral of SEUDisp22 is

begin
	process(Disp22)
		begin
			for i in 22 to 31 loop
				S(i)<=Disp22(21);
			end loop;
			S(21 downto 0)<=Disp22;
	end process;
end Behavioral;

