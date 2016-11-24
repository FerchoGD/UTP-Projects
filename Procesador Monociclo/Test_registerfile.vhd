LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
  
ENTITY Test_registerfile IS
END Test_registerfile;
 
ARCHITECTURE behavior OF Test_registerfile IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT register_file
    PORT(
			rst : IN  STD_LOGIC;
         rs1 : IN  std_logic_vector(4 downto 0);
         rs2 : IN  std_logic_vector(4 downto 0);
         rd : IN  std_logic_vector(4 downto 0);
         data : IN  std_logic_vector(31 downto 0);
         crs1 : OUT  std_logic_vector(31 downto 0);
         crs2 : OUT  std_logic_vector(31 downto 0)
        );
    END COMPONENT;
    

   --Inputs
	signal rst : std_logic;
   signal rs1 : std_logic_vector(4 downto 0) := (others => '0');
   signal rs2 : std_logic_vector(4 downto 0) := (others => '0');
   signal rd : std_logic_vector(4 downto 0) := (others => '0');
   signal data : std_logic_vector(31 downto 0) := (others => '0');

 	--Outputs
   signal crs1 : std_logic_vector(31 downto 0);
   signal crs2 : std_logic_vector(31 downto 0);
   -- No clocks detected in port list. Replace <clock> below with 
   -- appropriate port name 
  
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: register_file PORT MAP (
			 rst => rst,
          rs1 => rs1,
          rs2 => rs2,
          rd => rd,
          data => data,
          crs1 => crs1,
          crs2 => crs2
        );

   -- Clock process definitions


   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
		data <= x"FFFFFFFF";
		rd <= "00000";
      wait for 10 ns;
		data <= x"AAAAAAAA";
		rd <= "00001";
      wait for 10 ns;
		data <= x"BBBBBBBB";
		rd <= "00010";
      wait for 10 ns;
		data <= x"CCCCCCCC";
		rd <= "00011";
      wait for 10 ns;
		rs1 <= "00010";
		rs2 <= "00011";
		wait for 10 ns;
		rst <= '1';

      -- insert stimulus here 

      wait;
   end process;

END;
