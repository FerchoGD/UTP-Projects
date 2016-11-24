--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   16:20:42 10/06/2016
-- Design Name:   
-- Module Name:   C:/Users/utp.CRIE/Desktop/sparcv8-monocicle/Test_signExtUnit.vhd
-- Project Name:  monocicle-sparcv8
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: sign_ext_unit
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
 
ENTITY Test_signExtUnit IS
END Test_signExtUnit;
 
ARCHITECTURE behavior OF Test_signExtUnit IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT sign_ext_unit
    PORT(
         entrada : IN  std_logic_vector(12 downto 0);
         salida : OUT  std_logic_vector(31 downto 0)
        );
    END COMPONENT;
    

   --Inputs
   signal entrada : std_logic_vector(12 downto 0) := (others => '0');

 	--Outputs
   signal salida : std_logic_vector(31 downto 0);
   -- No clocks detected in port list. Replace <clock> below with 
   -- appropriate port name 
 
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: sign_ext_unit PORT MAP (
          entrada => entrada,
          salida => salida
        );


 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
		entrada <= "1111111111111";
      wait for 100 ns;	
		entrada <= "0011111111111";
      wait for 100 ns;	
		entrada <= "1010101010101";
      wait for 100 ns;	
		


      -- insert stimulus here 

      wait;
   end process;

END;
