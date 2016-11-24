library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;



entity DataMemory is
    Port ( enableMem : in  STD_LOGIC;
			  reset : in STD_LOGIC;
			  cRD : in  STD_LOGIC_VECTOR (31 downto 0);
           address : in STD_LOGIC_VECTOR (31 downto 0);				
           wrEnMem : in  STD_LOGIC;
           datoToWr : out  STD_LOGIC_VECTOR (31 downto 0)
			  );
end DataMemory;

architecture arqDataMemory of DataMemory is
	type ram_type is array (0 to 63) of std_logic_vector (31 downto 0);
	signal ramMemory : ram_type:=(others => x"00000000");
begin

	process(enableMem,reset,cRD,address,wrEnMem)
	begin
			if(enableMem = '1') then
				if(reset = '1')then
					datoToWr <= (others => '0');
					ramMemory <= (others => x"00000000");
				else
					if(wrEnMem = '0')then
						datoToWr <= ramMemory(conv_integer(address(5 downto 0)));
					else
						ramMemory(conv_integer(address(5 downto 0))) <= cRD;
					end if;
				end if;
			end if;
	end process;
end arqDataMemory;

