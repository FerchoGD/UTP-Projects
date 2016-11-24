LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY Test_instructionMemory IS
END Test_instructionMemory;
 
ARCHITECTURE behavior OF Test_instructionMemory IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT instructionMemory
    PORT(
         address : IN  std_logic_vector(3 downto 0);
         reset : IN  std_logic;
         clkFPGA : IN  std_logic;
         outInstruction : OUT  std_logic_vector(31 downto 0)
        );
    END COMPONENT;
    

   --Inputs
   signal address : std_logic_vector(3 downto 0) := (others => '0');
   signal reset : std_logic := '0';
   signal clkFPGA : std_logic := '0';

 	--Outputs
   signal outInstruction : std_logic_vector(31 downto 0);

   -- Clock period definitions
   constant clkFPGA_period : time := 20 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: instructionMemory PORT MAP (
          address => address,
          reset => reset,
          clkFPGA => clkFPGA,
          outInstruction => outInstruction
        );

   -- Clock process definitions
   clkFPGA_process :process
   begin
		clkFPGA <= '0';
		wait for clkFPGA_period/2;
		clkFPGA <= '1';
		wait for clkFPGA_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
		reset<='1';
		address <= "0000";
      wait for 100 ns;	
		reset<='0';
		address <= "1110";
      wait;
   end process;

END;