library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Sparcv8Monocicle is 
Port ( CLK : in  STD_LOGIC;
RST: in STD_LOGIC;
R : out  STD_LOGIC_VECTOR(31 downto 0)
			  );
end Sparcv8Monocicle;

architecture Behavioral of Sparcv8Monocicle is

---Componentes

COMPONENT windows_manager
	PORT(
		cwp : IN std_logic;
		rs1 : IN std_logic_vector(4 downto 0);
		rs2 : IN std_logic_vector(4 downto 0);
		rd : IN std_logic_vector(4 downto 0);
		op : IN std_logic_vector(1 downto 0);
		op3 : IN std_logic_vector(5 downto 0);          
		nrs1 : OUT std_logic_vector(5 downto 0);
		nrs2 : OUT std_logic_vector(5 downto 0);
		nrd : OUT std_logic_vector(5 downto 0);
		ncwp : OUT std_logic
		);
	END COMPONENT;

COMPONENT psr
	PORT(
		clk : IN std_logic;
		reset : IN std_logic;
		nzvc : IN std_logic_vector(3 downto 0);
		ncwp : IN std_logic;
		carry : OUT std_logic;
		cwp : OUT std_logic
		);
	END COMPONENT;
	
COMPONENT psr_modifier
	PORT(
		crs1 : IN std_logic;
		ope2 : IN std_logic;
		alur : IN std_logic_vector(31 downto 0);
		aluop : IN std_logic_vector(5 downto 0);          
		nzvc : OUT std_logic_vector(3 downto 0)
		);
	END COMPONENT;

COMPONENT sum32b
	PORT(
		Op1 : IN std_logic_vector(31 downto 0);
		Op2 : IN std_logic_vector(31 downto 0);          
		R : OUT std_logic_vector(31 downto 0)
		);
	END COMPONENT;

COMPONENT alu
	PORT(
		carry : IN std_logic;
		aluop : IN std_logic_vector(5 downto 0);
		crs1 : IN std_logic_vector(31 downto 0);
		crs2 : IN std_logic_vector(31 downto 0);          
		r : OUT std_logic_vector(31 downto 0)
		);
	END COMPONENT;
	

COMPONENT control_unit
	PORT(
		op : IN std_logic_vector(1 downto 0);
		op2 : IN std_logic_vector(2 downto 0);
		op3 : IN std_logic_vector(5 downto 0);
		icc : IN std_logic_vector(3 downto 0);
		cond : IN std_logic_vector(3 downto 0);          
		Aluop : OUT std_logic_vector(5 downto 0);
		wrenDM : OUT std_logic;
		RFSource : OUT std_logic_vector(1 downto 0);
		PCSource : OUT std_logic_vector(1 downto 0);
		RFdest : OUT std_logic;
		write_enable : OUT std_logic
		);
	END COMPONENT;
	

	
COMPONENT instructionMemory
	PORT(
		address : IN std_logic_vector(31 downto 0);
		reset : IN std_logic;          
		outInstruction : OUT std_logic_vector(31 downto 0)
		);
	END COMPONENT;

COMPONENT mux32b
	PORT(
		A : IN std_logic_vector(31 downto 0);
		B : IN std_logic_vector(31 downto 0);
		Sel : IN std_logic;          
		O : OUT std_logic_vector(31 downto 0)
		);
	END COMPONENT;

COMPONENT pc
	PORT(
		clk : IN std_logic;
		rst : IN std_logic;
		address : IN std_logic_vector(31 downto 0);          
		sig : OUT std_logic_vector(31 downto 0)
		);
	END COMPONENT;
	
	
COMPONENT register_file
	PORT(
		Wren : IN std_logic;
		rst : IN std_logic;
		rs1 : IN std_logic_vector(5 downto 0);
		rs2 : IN std_logic_vector(5 downto 0);
		rd : IN std_logic_vector(5 downto 0);
		data : IN std_logic_vector(31 downto 0);          
		crs1 : OUT std_logic_vector(31 downto 0);
		crs2 : OUT std_logic_vector(31 downto 0);
		crd : OUT std_logic_vector(31 downto 0)
		);
	END COMPONENT;
	
COMPONENT sign_ext_unit
	PORT(
		entrada : IN std_logic_vector(12 downto 0);          
		salida : OUT std_logic_vector(31 downto 0)
		);
	END COMPONENT;
	
COMPONENT SEUDisp30
	PORT(
		Disp30 : IN std_logic_vector(29 downto 0);          
		S : OUT std_logic_vector(31 downto 0)
		);
	END COMPONENT;
	
COMPONENT SEUDisp22
	PORT(
		Disp22 : IN std_logic_vector(21 downto 0);          
		S : OUT std_logic_vector(31 downto 0)
		);
	END COMPONENT;
	
COMPONENT MuxPC
	PORT(
		PCdisp30 : IN std_logic_vector(31 downto 0);
		PCdisp22 : IN std_logic_vector(31 downto 0);
		PC : IN std_logic_vector(31 downto 0);
		PCplus1 : IN std_logic_vector(31 downto 0);
		PCSource : IN std_logic_vector(1 downto 0);          
		nPC : OUT std_logic_vector(31 downto 0)
		);
	END COMPONENT;
	
COMPONENT MuxNextRD
	PORT(
		RD : IN std_logic_vector(5 downto 0);
		O7 : IN std_logic_vector(5 downto 0);
		RfDest : IN std_logic;          
		NRd : OUT std_logic_vector(5 downto 0)
		);
	END COMPONENT;
	
COMPONENT MuxDWR
	PORT(
		DM : IN std_logic_vector(31 downto 0);
		AluR : IN std_logic_vector(31 downto 0);
		PC : IN std_logic_vector(31 downto 0);
		RFSource : IN std_logic_vector(1 downto 0);          
		DTRF : OUT std_logic_vector(31 downto 0)
		);
	END COMPONENT;
	
COMPONENT DataMemory
	PORT(
		enableMem : IN std_logic;
		reset : IN std_logic;
		cRD : IN std_logic_vector(31 downto 0);
		address : IN std_logic_vector(31 downto 0);
		wrEnMem : IN std_logic;          
		datoToWr : OUT std_logic_vector(31 downto 0)
		);
	END COMPONENT;
	
signal aux1,aux2,aux3,aux4,aux6,aux7,aux9,aux10,aux11,aux20,aux21,aux22,aux23,aux25,aux29,aux30,aux32:std_logic_vector(31 downto 0);
signal aux5,aux14,aux15,aux16,aux27:std_logic_vector(5 downto 0);
signal aux12,aux17,aux18,aux26,aux28,aux31: std_logic;
signal aux24,aux34,aux33: std_logic_vector(1 downto 0);
signal aux13:std_logic_vector(3 downto 0);

begin

---Instancia de los componentes



	Inst_SEUDisp30: SEUDisp30 PORT MAP(
		Disp30 => aux4(29 downto 0),
		S => aux20
	);
	
	
	Inst_SEUDisp22: SEUDisp22 PORT MAP(
		Disp22 => aux4(21 downto 0),
		S => aux21
	);
	
	
	Inst_MuxPC: MuxPC PORT MAP(
		PCdisp30 => aux23,
		PCdisp22 => aux22,
		PC => aux3,
		PCplus1 => aux2,
		PCSource => aux24,
		nPC => aux25
	);
	
	
	Inst_MuxNextRD: MuxNextRD PORT MAP(
		RD => aux16,
		O7 => "001111",
		RfDest => aux26,
		NRd => aux27 
	);
	
	Inst_MuxDWR: MuxDWR PORT MAP(
		DM => aux32,
		AluR => aux30,
		PC => aux3,
		RFSource => aux33,
		DTRF => aux10
	);

	
	
	Inst_DataMemory: DataMemory PORT MAP(
		enableMem => '1',
		reset => RST,
		cRD => aux29,
		address => aux30,
		wrEnMem => aux31,
		datoToWr => aux32
	);
	
	
	

	Inst_windows_manager: windows_manager PORT MAP(
		cwp => aux18,
		rs1 => aux4(18 downto 14),
		rs2 => aux4(4 downto 0),
		rd => aux4(29 downto 25),
		op => aux4(31 downto 30),
		op3 => aux4(24 downto 19),
		nrs1 => aux14,
		nrs2 => aux15,
		nrd => aux16,
		ncwp => aux17
	);

	Inst_psr: psr PORT MAP(
		clk => CLK,
		reset => RST,
		nzvc => aux13,
		ncwp => aux17,
		carry => aux12,
		cwp => aux18
	);

	Inst_psr_modifier: psr_modifier PORT MAP(
		crs1 => aux6(31),
		ope2 => aux9(31),
		alur => aux30,
		aluop => aux5,
		nzvc => aux13
	);
	
	Inst_sumPC: sum32b PORT MAP(
		Op1 => x"00000001",
		Op2 => aux1,
		R => aux2 
	);
	
	Inst_sumDisp22: sum32b PORT MAP(
		Op1 => aux21,
		Op2 => aux3,
		R => aux22 
	);
	
	Inst_sumDisp30: sum32b PORT MAP(
		Op1 => aux20,
		Op2 => aux3,
		R => aux23 
	);
	
	Inst_alu: alu PORT MAP(
		carry => aux12,
		aluop => aux5,
		crs1 => aux6,
		crs2 => aux9,
		r => aux30
	);
	
	Inst_control_unit: control_unit PORT MAP(
		op => aux4(31 downto 30),
		op2 => aux4(24 downto 22),
		op3 => aux4(24 downto 19),
		icc => aux13,
		cond => aux4(28 downto 25),
		Aluop => aux5,
		wrenDM => aux31,
		RFSource => aux33,
		PCSource => aux24,
		RFdest => aux26,
		write_enable => aux28
	);
	
	Inst_instructionMemory: instructionMemory PORT MAP(
		address => aux3,
		reset => RST,
		outInstruction => aux4 
	);
	
	Inst_mux32b: mux32b PORT MAP(
		A => aux7,
		B => aux11,
		Sel => aux4(13),
		O => aux9
	);
	
	Inst_pc: pc PORT MAP(
		clk => CLK,
		rst => RST,
		address => aux1,
		sig => aux3
	);
	
	Inst_npc: pc PORT MAP(
		clk => CLK,
		rst => RST,
		address => aux25,
		sig => aux1
	);
	
	Inst_register_file: register_file PORT MAP(
		Wren => aux28,
		rst => RST,
		rs1 => aux14,
		rs2 => aux15,
		rd => aux27,
		data => aux10,
		crs1 => aux6,
		crs2 => aux7,
		crd => aux29
	);
	
	
	Inst_sign_ext_unit: sign_ext_unit PORT MAP(
		entrada => aux4(12 downto 0),
		salida => aux11
	);


	R<=aux30;

end Behavioral;


