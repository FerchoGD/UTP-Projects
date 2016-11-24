LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
  
ENTITY Test_sum32b IS
END Test_sum32b;
 
ARCHITECTURE behavior OF Test_sum32b IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT sum32b
    PORT(
         Op1 : IN  std_logic_vector(31 downto 0);
         Op2 : IN  std_logic_vector(31 downto 0);
         R : OUT  std_logic_vector(31 downto 0)
        );
    END COMPONENT;
    

   --Inputs
   signal Op1 : std_logic_vector(31 downto 0) := (others => '0');
   signal Op2 : std_logic_vector(31 downto 0) := (others => '0');

 	--Outputs
   signal R : std_logic_vector(31 downto 0);
   -- No clocks detected in port list. Replace <clock> below with 
   -- appropriate port name 
 
  
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: sum32b PORT MAP (
          Op1 => Op1,
          Op2 => Op2,
          R => R
        );

   -- Clock process definitions
  
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
		Op1 <= x"00000014";
		Op2 <= x"0000000A";
      wait for 100 ns;
		Op2 <= x"00000014";


      -- insert stimulus here 

      wait;
   end process;

END;
