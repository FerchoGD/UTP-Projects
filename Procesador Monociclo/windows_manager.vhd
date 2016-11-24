library IEEE;
use IEEE.NUMERIC_STD.ALL;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
use ieee.std_logic_arith.ALL;

entity windows_manager is
    Port ( cwp : in  STD_LOGIC;
			  rs1 : in  STD_LOGIC_VECTOR(4 downto 0);
           rs2 : in  STD_LOGIC_VECTOR(4 downto 0);
           rd : in  STD_LOGIC_VECTOR(4 downto 0);
           op : in  STD_LOGIC_VECTOR(1 downto 0);
           op3 : in  STD_LOGIC_VECTOR(5 downto 0);
           nrs1 : out  STD_LOGIC_VECTOR(5 downto 0);
           nrs2 : out  STD_LOGIC_VECTOR(5 downto 0);
           nrd : out  STD_LOGIC_VECTOR(5 downto 0);
           ncwp : out  STD_LOGIC
           );
end windows_manager;

architecture Behavioral of windows_manager is

signal rs1int,rs2int,rdint: integer range 0 to 39;
signal ncwp_signal: std_logic;

begin

	process(cwp,rs1,rs2,rd,op,op3,ncwp_signal)
	begin
		if(op = "10") then
			if(op3= "111100") then --Save (Resto)
				ncwp_signal<= '0';
			elsif(op3="111101") then --Restore (Sumo)
				ncwp_signal<= '1';
			else
				ncwp_signal<=cwp;
			end if;
		end if;
			
			if(rs1>="11000" and rs1<="11111") then--Formula registro de entrada (r[24] - r[31])
					rs1int <= conv_integer(rs1)-(conv_integer(cwp)*16);
			elsif(rs1>="10000" and rs1<="10111") then--Formula registro de local (r[16] - r[23])
					rs1int <= conv_integer(rs1)+(conv_integer(cwp)*16);
			elsif(rs1>="01000" and rs1<="01111") then--Formula registro de salida (r[8] - r[15])
					rs1int <= conv_integer(rs1)+ (conv_integer(cwp)*16);
			elsif(rs1>="00000" and rs1<="00111") then--Formula registro global (r[0] - r[7])
					rs1int <= conv_integer(rs1);
			end if;
			
			if(rs2>="11000" and rs2<="11111") then--Formula registro de entrada (r[24] - r[31])
					rs2int <= conv_integer(rs2)-(conv_integer(cwp)*16);
			elsif(rs2>="10000" and rs2<="10111") then--Formula registro de local (r[16] - r[23])
					rs2int <= conv_integer(rs2)+(conv_integer(cwp)*16);
			elsif(rs2>="01000" and rs2<="01111") then--Formula registro de salida (r[8] - r[15])
					rs2int <= conv_integer(rs2)+ (conv_integer(cwp)*16);
			elsif(rs2>="00000" and rs2<="00111") then--Formula registro global (r[0] - r[7])
					rs2int <= conv_integer(rs2);
			end if;
			
			if(rd>="11000" and rd<="11111") then--Formula registro de entrada (r[24] - r[31])
					rdint <= conv_integer(rd)-(conv_integer(ncwp_signal)*16);
			elsif(rd>="10000" and rd<="10111") then--Formula registro de local (r[16] - r[23])
					rdint <= conv_integer(rd)+(conv_integer(ncwp_signal)*16);
			elsif(rd>="01000" and rd<="01111") then--Formula registro de salida (r[8] - r[15])
					rdint <= conv_integer(rd)+ (conv_integer(ncwp_signal)*16);
			elsif(rd>="00000" and rd<="00111") then--Formula registro global (r[0] - r[7])
					rdint <= conv_integer(rd);
			end if;
			
	end process;
	
	nrs1 <= conv_std_logic_vector(rs1int, 6);
	nrs2 <= conv_std_logic_vector(rs2int, 6);
	nrd <= conv_std_logic_vector(rdint, 6);
	ncwp <= ncwp_signal;

end Behavioral;

