LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
 
ENTITY Test_PC IS
END Test_PC;
 
ARCHITECTURE behavior OF Test_PC IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT pc
    PORT(
         clk : IN  std_logic;
         rst : IN  std_logic;
         address : IN  std_logic_vector(31 downto 0);
         sig : OUT  std_logic_vector(31 downto 0)
        );
    END COMPONENT;
    

   --Inputs
   signal clk : std_logic := '0';
   signal rst : std_logic := '0';
   signal address : std_logic_vector(31 downto 0) := (others => '0');

 	--Outputs
   signal sig : std_logic_vector(31 downto 0);

   -- Clock period definitions
   constant clk_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: pc PORT MAP (
          clk => clk,
          rst => rst,
          address => address,
          sig => sig
        );

   -- Clock process definitions
   clk_process :process
   begin
		clk <= '0';
		wait for clk_period/2;
		clk <= '1';
		wait for clk_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
		address <= x"FFFFFFFF";
      wait for 200 ns;
		rst <= '1';
		wait for 100 ns;
		rst <= '0';
		wait for 50 ns;
		address <= x"11111111";
		


      -- insert stimulus here 

      wait;
   end process;

END;
