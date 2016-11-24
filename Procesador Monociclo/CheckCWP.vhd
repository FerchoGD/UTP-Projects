--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   22:56:44 10/26/2016
-- Design Name:   
-- Module Name:   C:/Users/Personal/Downloads/sparcv8-monocicle-master/CheckCWP.vhd
-- Project Name:  monocicle-sparcv8
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: Sparcv8Monocicle
-- 
-- Dependencies:
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
--
-- Notes: 
-- This testbench has been automatically generated using types std_logic and
-- std_logic_vector for the ports of the unit under test.  Xilinx recommends
-- that these types always be used for the top-level I/O of a design in order
-- to guarantee that the testbench will bind correctly to the post-implementation 
-- simulation model.
--------------------------------------------------------------------------------
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY CheckCWP IS
END CheckCWP;
 
ARCHITECTURE behavior OF CheckCWP IS 
 
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
      RST <= '1';
		wait for 2 ns;
		RST <= '0';
		wait ;
   end process;

END;
