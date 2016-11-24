library IEEE;
use IEEE.NUMERIC_STD.ALL;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity alu is
	Port( carry: in STD_LOGIC;
			aluop : in  STD_LOGIC_VECTOR (5  downto 0);
			crs1   : in  STD_LOGIC_VECTOR (31 downto 0); 
			crs2   : in  STD_LOGIC_VECTOR (31 downto 0);
			r     : out STD_LOGIC_VECTOR (31 downto 0)
	);
end alu;

architecture ArqAlu of alu is

begin
	process(aluop, crs1, crs2,carry)
	begin
		if (aluop="000000") or (aluop="001000") then --Add Operations
			r <= crs1 + crs2;
		elsif (aluop="001010") or (aluop="001011") then --AddX Operations
			r<=crs1 +crs2 + carry;
		elsif (aluop="000001") or (aluop="001001") then --Sub Operations
			r <= crs1 - crs2 ;
		elsif (aluop="001100") or (aluop="001101") then --SubX Operations
			r<=crs1 - crs2 - carry;
		elsif (aluop="000010") or (aluop="001110") then --Or Operations
			r <= crs1 or crs2;
		elsif (aluop="000011") or (aluop="001111") then --And Operations
			r <= crs1 and crs2;
		elsif (aluop="000101") or (aluop="010010") then --OrN Operations
			r <= crs1 or not(crs2);
		elsif (aluop="000100") or (aluop="010000") then --Xor Operations
			r <= crs1 xor crs2;
		elsif (aluop="000110") or (aluop="010001") then --AndN Operations
			r <= crs1 and not(crs2);
		elsif (aluop="000111") or (aluop="010011") then --Xnor Operations
			r <= crs1 xnor crs2;
		elsif (aluop="010100")then --SLL
			r<= to_stdlogicvector(to_bitvector(crs1) SLL conv_integer(crs2));
		elsif (aluop="010101")then --SRL
			r<= to_stdlogicvector(to_bitvector(crs1) SRL conv_integer(crs2));
		else
			r<=x"00000000";
		end if;
	end process;

end ArqAlu;





