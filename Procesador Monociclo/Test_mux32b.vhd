LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
 
ENTITY Test_mux32b IS
END Test_mux32b;
 
ARCHITECTURE behavior OF Test_mux32b IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT mux32b
    PORT(
         A : IN  std_logic_vector(31 downto 0);
         B : IN  std_logic_vector(31 downto 0);
         Sel : IN  std_logic;
         O : OUT  std_logic_vector(31 downto 0)
        );
    END COMPONENT;
    

   --Inputs
   signal A : std_logic_vector(31 downto 0) := (others => '0');
   signal B : std_logic_vector(31 downto 0) := (others => '0');
   signal Sel : std_logic := '0';

 	--Outputs
   signal O : std_logic_vector(31 downto 0);

 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: mux32b PORT MAP (
          A => A,
          B => B,
          Sel => Sel,
          O => O
        );

   -- Clock process definitions
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      A <= x"FFFFFFFF";
		B <= x"00000000";
		wait for 100 ns;
		Sel <= '1';
		wait for 100 ns;
		Sel <= '0';
		wait for 100 ns;
		Sel <= '1';
		wait for 100 ns;
		Sel <= '0';
		
		
      -- insert stimulus here 

      wait;
   end process;

END;
