library IEEE;
use IEEE.STD_LOGIC_1164.ALL;


entity psr_modifier is
	Port( crs1 : in std_logic;
	      ope2 : in std_logic;
			alur : in STD_LOGIC_VECTOR(31 downto 0);
			aluop : in std_logic_vector(5 downto 0);
			nzvc : out std_logic_vector(3 downto 0)
	);
end psr_modifier;

architecture psr_modArq of psr_modifier is

begin

process(crs1, ope2, alur, aluop)
begin

	-- ADDcc y ADDxcc
	if (aluop = "001000" or aluop = "01011") then
		nzvc(3) <= alur(31);
		if (alur = x"00000000") then nzvc(2) <= '1'; else nzvc(2) <= '0'; end if;
		nzvc(1) <= (crs1 and ope2 and (not alur(31))) or ((not crs1) and (not ope2) and alur(31));
		nzvc(0) <= (crs1 and ope2) or ((not alur(31)) and (crs1 or ope2));
	-- SUBcc y SUBxcc
	else 
		if (aluop = "001001" or aluop = "001101")then
			nzvc(3) <= alur(31);
			if (alur = x"00000000") then nzvc(2) <= '1'; else nzvc(2) <= '0'; end if;
			nzvc(1) <= (crs1 and (not ope2) and (not alur(31))) or ((not crs1) and ope2 and alur(31));
			nzvc(0) <= ((not crs1) and ope2) or (alur(31) and ((not crs1) or ope2));
		--ANDcc, ANDNcc, ORcc, ORNcc, XORcc, XNORcc
		else
			if (aluop = "001111" or aluop = "010001" or aluop = "001110" or aluop = "010010" or aluop = "010000" or aluop = "010011")then
				nzvc(3) <= alur(31);
				if (alur = x"00000000") then nzvc(2) <= '1'; else nzvc(2) <= '0'; end if;
				nzvc(1) <= '0';
				nzvc(0) <= '1';
			end if;
		end if;
	end if;
	
end process;


end psr_modArq;

