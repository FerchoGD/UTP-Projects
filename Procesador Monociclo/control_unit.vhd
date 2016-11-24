library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity control_unit is
    Port ( 
			  op : in  STD_LOGIC_VECTOR (1 downto 0);
			  op2 : in STD_LOGIC_VECTOR (2 downto 0);
			  op3 : in  STD_LOGIC_VECTOR (5 downto 0);
			  icc : in STD_LOGIC_VECTOR (3 downto 0);
			  cond: in STD_LOGIC_VECTOR (3 downto 0);
			  Aluop: out STD_LOGIC_VECTOR (5 downto 0);
			  wrenDM: out STD_LOGIC;
			  RFSource:  out STD_LOGIC_VECTOR(1 downto 0);
			  PCSource: out STD_LOGIC_VECTOR(1 downto 0);
			  RFdest: out STD_LOGIC;
			  write_enable : out STD_LOGIC);

end control_unit;
 
architecture arq_UnidadControl of control_unit is

begin
	process(op,op2,op3,icc,cond)
	begin
	if(op = "01") then --CALL
		PCSource<= "01";--PC + disp30
		write_enable <= '1';--Permitimos guardar datos en RF (Valor actual de PC)
		RFSource<= "10";--Elegimos PC
		RFdest<='1';--Se debe elegir el O7 en el RF
		wrenDM <= '0';--No escribimos en DM
		Aluop <= "111111";--No hacemos operaciones aritmetico logicas
	else
		if(op= "00") then
			if(op2= "010") then
				case cond is
					when "1000" => --Branch Always
						PCSource<= "10";--PC + seu(disp22)
						write_enable <= '0';--No Permitimos guardar datos en RF 
						RFSource<= "00";--Elegimos aluresult
						RFdest<='0';--Se debe elegir nRd
						wrenDM <= '0';--No escribimos en DM
						Aluop <= "111111";--No hacemos operaciones aritmetico logicas
					when "1001" => --Branch on Not Equal
						if(not(icc(2)) = '1') then --not z
							PCSource<= "10";--PC + seu(disp22)
							write_enable <= '0';--No Permitimos guardar datos en RF 
							RFSource<= "00";--Elegimos aluresult
							RFdest<='0';--Se debe elegir nRd
							wrenDM <= '0';--No escribimos en DM
							Aluop <= "111111";--No hacemos operaciones aritmetico logicas
						else
							PCSource<= "11";--PC + 1
							write_enable <= '0';--No Permitimos guardar datos en RF 
							RFSource<= "00";--Elegimos aluresult
							RFdest<='0';--Se debe elegir nRd
							wrenDM <= '0';--No escribimos en DM
							Aluop <= "111111";--No hacemos operaciones aritmetico logicas
						end if;
					when "0001" => --Branch on Equal
						if(icc(2) = '1') then
							PCSource<= "10";--PC + seu(disp22)
							write_enable <= '0';--No Permitimos guardar datos en RF 
							RFSource<= "00";--Elegimos aluresult
							RFdest<='0';--Se debe elegir nRd
							wrenDM <= '0';--No escribimos en DM
							Aluop <= "111111";--No hacemos operaciones aritmetico logicas
						else
							PCSource<= "11";--PC + 1
							write_enable <= '0';--No Permitimos guardar datos en RF 
							RFSource<= "00";--Elegimos aluresult
							RFdest<='0';--Se debe elegir nRd
							wrenDM <= '0';--No escribimos en DM
							Aluop <= "111111";--No hacemos operaciones aritmetico logicas
						end if;
					when "1010" => --Branch on Greater
						if((not(icc(2) or (icc(3) xor icc(1)))) = '1') then --not(Z or (N xor V))
							PCSource<= "10";--PC + seu(disp22)
							write_enable <= '0';--No Permitimos guardar datos en RF 
							RFSource<= "00";--Elegimos aluresult
							RFdest<='0';--Se debe elegir nRd
							wrenDM <= '0';--No escribimos en DM
							Aluop <= "111111";--No hacemos operaciones aritmetico logicas
						else
							PCSource<= "11";--PC + 1
							write_enable <= '0';--No Permitimos guardar datos en RF 
							RFSource<= "00";--Elegimos aluresult
							RFdest<='0';--Se debe elegir nRd
							wrenDM <= '0';--No escribimos en DM
							Aluop <= "111111";--No hacemos operaciones aritmetico logicas
						end if;
					when "0010" => --Branch on Less or Equal
						if((icc(2) or (icc(3) xor icc(1))) = '1') then --Z or (N xor V)
							PCSource<= "10";--PC + seu(disp22)
							write_enable <= '0';--No Permitimos guardar datos en RF 
							RFSource<= "00";--Elegimos aluresult
							RFdest<='0';--Se debe elegir nRd
							wrenDM <= '0';--No escribimos en DM
							Aluop <= "111111";--No hacemos operaciones aritmetico logicas
						else
							PCSource<= "11";--PC + 1
							write_enable <= '0';--No Permitimos guardar datos en RF 
							RFSource<= "00";--Elegimos aluresult
							RFdest<='0';--Se debe elegir nRd
							wrenDM <= '0';--No escribimos en DM
							Aluop <= "111111";--No hacemos operaciones aritmetico logicas
						end if;
					when "1011" => -- Branch on Greater or Equal
						if((not(icc(3) xor icc(1))) = '1') then --not (N xor V)
							PCSource<= "10";--PC + seu(disp22)
							write_enable <= '0';--No Permitimos guardar datos en RF 
							RFSource<= "00";--Elegimos aluresult
							RFdest<='0';--Se debe elegir nRd
							wrenDM <= '0';--No escribimos en DM
							Aluop <= "111111";--No hacemos operaciones aritmetico logicas
						else
							PCSource<= "11";--PC + 1
							write_enable <= '0';--No Permitimos guardar datos en RF 
							RFSource<= "00";--Elegimos aluresult
							RFdest<='0';--Se debe elegir nRd
							wrenDM <= '0';--No escribimos en DM
							Aluop <= "111111";--No hacemos operaciones aritmetico logicas
						end if;
					when "0011" => --Branch on Less
						if((icc(3) xor icc(1)) = '1') then -- (N xor V)
							PCSource<= "10";--PC + seu(disp22)
							write_enable <= '0';--No Permitimos guardar datos en RF 
							RFSource<= "00";--Elegimos aluresult
							RFdest<='0';--Se debe elegir nRd
							wrenDM <= '0';--No escribimos en DM
							Aluop <= "111111";--No hacemos operaciones aritmetico logicas
						else
							PCSource<= "11";--PC + 1
							write_enable <= '0';--No Permitimos guardar datos en RF 
							RFSource<= "00";--Elegimos aluresult
							RFdest<='0';--Se debe elegir nRd
							wrenDM <= '0';--No escribimos en DM
							Aluop <= "111111";--No hacemos operaciones aritmetico logicas
						end if;
					when others =>
						PCSource<= "11";--PC + PCaddress
						write_enable <= '0';--No Permitimos guardar datos en RF 
						RFSource<= "00";--Elegimos aluresult
						RFdest<='0';--Se debe elegir nRd
						wrenDM <= '0';--No escribimos en DM
						Aluop <= "111111";--No hacemos operaciones aritmetico logicas
				end case;
			elsif(op2 = "100") then --NOP
				PCSource<= "11";--PC + 1
				write_enable <= '0';--No Permitimos guardar datos en RF (Valor actual de PC)
				RFSource<= "00";--Elegimos aluresult
				RFdest<='0';--Se debe elegir nRd
				wrenDM <= '0';--No escribimos en DM
				Aluop <= "111111";--No hacemos operaciones aritmetico logicas
			end if;
		elsif(op = "10")then				
			case op3 is
				when "000000" => -- ADD
					Aluop <= "000000";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "010000" => --ADDcc
					Aluop <= "001000";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "001000" => --ADDX
					Aluop <= "001010";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "011000" => --ADDXcc
					Aluop <= "001011";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "000100" => -- SUB
					Aluop <= "000001";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "010100" => -- SUBcc
					Aluop <= "001001";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "001100" => -- SUBX
					Aluop <= "001100";
					write_enable <= '1';
					RFSource<= "00";
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
					
				when "011100" => -- SUBXcc
					Aluop <= "001101";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "000001" => -- AND
					Aluop <= "000011";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "010001" => -- ANDcc
					Aluop <= "001111";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "000101" => --ANDN
					Aluop <= "000110";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
				when "010101" => --ANDNcc
					Aluop <= "010001";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "000010" => -- OR
					Aluop <= "000010";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "010010" => -- ORcc
					Aluop <= "001110";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "000110" => --ORN
					Aluop <= "000101";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "010110" => --ORNcc
					Aluop <= "010010";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "000011" => -- XOR
					Aluop <= "000100";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "010011" => -- XORcc
					Aluop <= "010000";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "000111" => -- XNOR
					Aluop <= "000111";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "010111" => -- XNORcc
					Aluop <= "010011";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "111100" => -- SAVE
					Aluop <= "000000";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "111101" => -- RESTORE
					Aluop <= "000000";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "111000" => --JMPL
					Aluop <= "000000";
					write_enable <= '1';
					wrenDM <= '0';
					RFSource<= "10";
					PCSource<= "00";--PC calculada
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "100101" => --SLL
					Aluop <= "010100";
					write_enable <= '0';
					wrenDM <= '0';
					RFSource<= "10";
					PCSource<= "00";
					RFdest<='0';
				when "100110" => --SRL
					Aluop <= "010101";
					write_enable <= '0';
					wrenDM <= '0';
					RFSource<= "10";
					PCSource<= "00";
					RFdest<='0';
				when others => --En otros casos desconocidos
					Aluop <= "111111";
					write_enable <= '0';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
			end case;
		elsif(OP = "11") then
			case op3 is
				when "000100" => --SW
					Aluop <= "000000";
					write_enable <= '0';
					wrenDM <= '1';--Habilitamos la escritura en el DM
					RFSource <= "00";
					PCSource <= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				when "000000" => --LW
					Aluop <= "000000";
					write_enable <= '1';--Habilitamos la escritura en el RF
					wrenDM <= '0';--Si no habilitamos la escritura, es porque vamos a leer
					RFSource <= "01";
					PCSource <= "11";--Se salta a PC + 1
					RFdest <='0';--Se debe elegir el nrd en el RF
				when others =>
					Aluop <= "000000";
					write_enable <= '0';
					wrenDM <= '0';
					RFSource<= "00";
					PCSource<= "11";--Se salta a PC + 1
					RFdest<='0';--Se debe elegir el nrd en el RF
				end case;
		end if;
	end if;
end process;

end arq_UnidadControl;



