library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity sum32b is
    Port ( Op1 : in  STD_LOGIC_VECTOR (31 downto 0);
           Op2 : in  STD_LOGIC_VECTOR (31 downto 0);
           R : out  STD_LOGIC_VECTOR (31 downto 0));
end sum32b;

architecture ArqSum32 of sum32b is

begin

	process(Op1, Op2)
	begin
		R <= Op1 + Op2;
	end process;

end ArqSum32;

