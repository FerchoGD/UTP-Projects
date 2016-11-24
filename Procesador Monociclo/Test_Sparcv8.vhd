LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY Test_Sparcv8 IS
END Test_Sparcv8;
 
ARCHITECTURE behavior OF Test_Sparcv8 IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT Sparcv8Monocicle
    PORT(
         CLK : IN  std_logic;
         RST : IN  std_logic;
         R : OUT  std_logic_vector(31 downto 0);
         CWPCheck : OUT  std_logic
        );
    END COMPONENT;
    

   --Inputs
   signal CLK : std_logic := '0';
   signal RST : std_logic := '0';

 	--Outputs
   signal R : std_logic_vector(31 downto 0);
   signal CWPCheck : std_logic;

   -- Clock period definitions
   constant CLK_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: Sparcv8Monocicle PORT MAP (
          CLK => CLK,
          RST => RST,
          R => R,
          CWPCheck => CWPCheck
        );

   -- Clock process definitions
   CLK_process :process
   begin
		CLK <= '0';
		wait for CLK_period/2;
		CLK <= '1';
		wait for CLK_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for CLK_period*10;

      -- insert stimulus here 

      wait;
   end process;

END;
